import requests
import json

def post_request(url,auth,header,payload, in_json):
    post_response_data = requests.post(url=url,headers= header, auth =auth, data =json.dumps(payload))
    if in_json is True:
        return post_response_data.json()
    return post_response_data


def put_data(url,auth,header,payload, in_json):
    patch_response_data = requests.put(url=url,headers= header, auth =auth, data =json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data


def get_request(url,auth,header, in_json):
    response = requests.get(url=url,headers= header, auth =auth)
    if in_json is True:
        return response.json()
    return response


def delete_request(url,auth,header, in_json):
    delete_response_data = requests.delete(url=url,headers= header,  auth =auth )
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data


