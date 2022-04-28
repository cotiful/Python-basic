import json

# 파이썬의 언어 규칙 
json_str = '''
{"id":1,"username":"cos","password":"1234"}
'''

#json -> dict
dic1 = json.loads(json_str)
print(dic1)
print(dic1["password"])

#dict -> json
dict_to_json=json.dumps(dic1)
print(dict_to_json)