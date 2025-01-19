import requests

def get_json_data(id):
    res = requests.get(f'https://xxx', params={'id': id})
    res_json = res.json()
    return res_json

def get_user_name(user_ids):
    user_names = {}
    for id in user_ids:
        res_json = get_json_data(id)
        user_names[id] = res_json['name']
    return user_names

def user_name_validation(user_name):
    if user_name == None:
        raise ValueError('名前が設定されていません')