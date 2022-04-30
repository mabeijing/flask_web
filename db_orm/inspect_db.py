import random

from db_orm.mysql_table import TBUser, TBRequest
import requests

"""
data = {xxx}
"""
data = {'user_id': 400, 'user_name': 'houn'}
# User(**data).save()

user1 = TBUser(**data)


# d = TBUser.query(user1)
# print(d.to_dict())

#
# req = TBRequest()
# req.NAME = 'project_search'
# req.DESC = 'desc'
# req.URL = 'url'
# req.METHOD = 'POST'
# req.HEADERS = {'session': '', 'content_type': 'application/json'}
# req.BODY = {"page": 1, "pageSize": 9}
#
# req.save()

def add_a_request():
    req = TBRequest()
    req.NAME = 'project_search' + str(random.random())
    req.DESC = 'desc'
    req.URL = ''
    req.METHOD = 'POST'
    req.HEADERS = {'session': '', 'content_type': 'application/json'}
    req.BODY = {"page": 1, "pageSize": 9}

    req.save()


def get_request(name):
    req = TBRequest.query(name)
    return req


if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor, as_completed

    executor = ThreadPoolExecutor(max_workers=5)
    tasks = []
    project = ['project_search',
               'project_search0.29361199186874076',
               'project_search0.6784162597291346',
               'project_search0.4975181358634032',
               'project_search0.980955867349281',
               'project_search0.7137833111562872',
               'project_search0.4544916705309019',
               'project_search0.1076863101802481',
               'project_search0.8311422698233081',
               'project_search0.48545192522512903',
               'project_search0.010527422327866631'
               ]
    for name in project:
        tasks.append(executor.submit(get_request, name))

    for future in as_completed(tasks):
        data = future.result()
        print(data)

# req = TBRequest.query(name='project_search')

# print(req)
# url = req.URL
# method = req.METHOD
# headers = req.HEADERS
# body = req.BODY
#
# response = requests.request(method, url, headers=headers, json=body)
# print(response.json())
