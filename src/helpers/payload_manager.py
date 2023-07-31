def payload_create_token():
    # In future you can replace this from the excel or JSON
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload


def payload_create_booking():
    # In future you can replace this from the excel or JSON
    payload = {
    "firstname" : "supriya",
    "lastname" : "sup",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    return payload

def patch_update():
    payload = {
        "firstname": "Nithya",
        "lastname": "nith",
        "totalprice": 143,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload