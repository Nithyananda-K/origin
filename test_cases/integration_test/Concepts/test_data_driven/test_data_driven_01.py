# read the data from the excel file
# pass the data one by one, and run the test_post_create_token,
# how row in the excel file  5 times -Row


import pytest
import requests


def test_post_create_token():
    payload = {
    "username": "admin",
    "password": "password123"
    }
    header = {
    "Content-Type" : "application/json"
    }
    response = requests.post("https://restful-booker.herokuapp.com/auth", headers=header, json=payload)
    # verify expected result = actual result
    # assert response.status_code == 200
    # print(response.text)
    token = response.json()["token"]
    print("your token is --> "+ str(token))
    return token