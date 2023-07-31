# help to read the json files and provide you the json data
import json


def get_payload_auth():
    # read from the auth.json and return json
    file_data = open("src/resources/auth.json")
    data = json.JSONEncoder(file_data)
    file_data.close()
    return data

def common_headers():
    headers = {
        "Content-Type": "application/json"
    }
    return headers

def token_headers(create_token):
    Token_here = "token=" + str(create_token)
    headers = {
        "Content-Type": "application/json",
        "Cookie": Token_here
    }
    return headers