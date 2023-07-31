# add your constants her ( URL )
# adding my URL constants.  python--> functions

def base_url():
    # change based on the env.json- stage, preprod, prod
    # In future I will write a login to change the base url based on the env 
    return "https://restful-booker.herokuapp.com"
    # beta -"https://beta-restful-booker.herokuapp.com"
    # prod -"https://prod-restful-booker.herokuapp.com"

def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


def url_update_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/"+ str(booking_id)


def url_get_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/"+ str(booking_id)