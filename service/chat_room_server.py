from threading import Lock
from . import socket_io
from flask import session, request, copy_current_request_context
from flask_socketio import (emit, join_room, leave_room,
                            close_room, rooms, disconnect)
from async_tasks.tasks import socket_bar
from celery.result import AsyncResult

count = 1

thread = None
thread_lock = Lock()


def socket_banner():
    task_result = socket_bar.delay()
    task_id = task_result.id
    res = AsyncResult(task_id)
    while res.status != 'SUCCESS':
        global count
        socket_io.sleep(1)
        if not isinstance(res.result, dict):
            continue
        socket_io.emit('my_response', {'data': '任务进度: {0}%'.format(res.result.get('p')), 'count': count})
        res = AsyncResult(task_id)
        count = count + 1

    if res.result == 'finish':
        socket_io.emit('my_response', {'data': f'任务进度: 100%'})


def background_thread():
    """Example of how to send server generated events to clients."""
    global count

    while True:
        socket_io.sleep(10)
        count += 1
        socket_io.emit('my_response', {'data': 'Start background_thread', 'count': count})


# Echo
@socket_io.event
def echo_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    # global thread
    # with thread_lock:
    #     if thread is None:
    #         thread = socket_io.start_background_task(socket_banner)
    socket_io.start_background_task(socket_banner)
    emit('my_response', {'data': message['data'], 'count': session['receive_count']})


# Broadcast
@socket_io.event
def broadcast_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@socket_io.event
def join(message):
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socket_io.event
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socket_io.on('close_room')
def on_close_room(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.',
                         'count': session['receive_count']},
         to=message['room'])
    close_room(message['room'])


@socket_io.event
def my_room_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         to=message['room'])


@socket_io.event
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    session['receive_count'] = session.get('receive_count', 0) + 1
    # for this emit we use a callback function
    # when the callback function is invoked we know that the message has been
    # received and it is safe to disconnect
    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']},
         callback=can_disconnect)


@socket_io.event
def my_ping():
    emit('my_pong')


@socket_io.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socket_io.start_background_task(background_thread)
    print('new Client connected: ', request.sid)
    emit('my_response', {'data': 'Connected success!', 'count': 0})


@socket_io.on('disconnect')
def disconnect_conn():
    print('new Client disconnected: ', request.sid)
