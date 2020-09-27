import re
import json

a = {
    'name': 'login',
    'url': '%(BASE_URL)s/login',
    'data': {
        'username': '%(username)s',
        'password': '%(password)s',
        'meta': {
            'require': True,
            'default': None
        }
    }
}

aa = {'BASE_URL': 'http://www.baidu.com', 'username': 'mabeijing', 'password': '123456'}


class MyDict(dict):
    FLAG = '**##**'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.args = kwargs
        self.target_dict = {}

    def _replace_re_data(self, matched):
        pass

    def __call__(self, **kwargs):
        for key, value in self.args.items():
            if isinstance(value, (dict, MyDict)):
                self.args = value
                self.__call__(**kwargs)
            else:
                pattern = re.compile('%(.+)s')

                match = pattern.search(str(value))
                if match:
                    result = match.group()
                    transport_value = value.replace(result, MyDict.FLAG)
                    for Key, Value in kwargs.items():
                        tmp = {Key: Value}
                        if result[2:-2] == Key:
                            values = transport_value.replace(MyDict.FLAG, match.group() % tmp)
                            self.target_dict[key] = values
                else:
                    self.target_dict[key] = value
        return json.loads(json.dumps(self.target_dict))


b = MyDict(**a)
ss = b(**aa)
print(ss)
print(type(ss))
