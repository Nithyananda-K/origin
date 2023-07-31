import os

from dotenv import load_dotenv
import pytest
import dotenv
import requests

# get all booking id
def test_get_req():
    response = requests.get("https://restful-booker.herokuapp.com/booking")
    # print(response.text)
    # J_R= response.headers
    # print(J_R.items())
    get_res = response.status_code
    print("your status  " + str(get_res))
    # assert response.status_code == 200
    assert len(response.json()) > 0

# create auth Token
@pytest.fixture()
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
    # print(token)
    return token

     # create booking
@pytest.fixture()
def test_create_booking_id():
    payload = {
    "firstname" : "supriya",
    "lastname" : "Nith",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    header = {
    "Content-Type" : "application/json"
    }
    response = requests.post("https://restful-booker.herokuapp.com/booking", headers=header, json=payload,)
    # verify expected result = actual result

    assert response.status_code == 200
    # print(response.json()["bookingid"])
    book_id = response.json()["bookingid"]
    print("your booking id " +str(book_id))
    return book_id

def test_update_booking(test_post_create_token, test_create_booking_id):
    payload_update = {
        "firstname": "NityaSuper",
        "lastname": "Nith",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    load_dotenv()
    auth_token = "token="+ os.getenv("token")
    print(auth_token)

    header = {
        "Content-Type": "application/json",
        "Cookie": auth_token
    }
    url_put = "https://restful-booker.herokuapp.com/booking/"+str(test_create_booking_id)
    response = requests.put(url_put, headers=header, json=payload_update )
    # print(response.text)
    print(response.json()["firstname"])

    # assert response.status_code==200

def test_delete_req(test_post_create_token,test_create_booking_id):
    auth_token = "token="+str(test_post_create_token)
    header = {
        "Content-Type": "application/json",
        "Cookie": auth_token
    }
    response = requests.delete("https://restful-booker.herokuapp.com/booking/"+str(test_create_booking_id), headers=header)
    print(response.text)
    print(response.status_code)
    # assert response.status_code == 200

