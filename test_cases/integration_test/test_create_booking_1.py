"""
objective : Create & verify by post Request
TC_01 - Verify the status code, headers
TC_02 - Verify the Body --> Booking ID
TC_03 - Verify the JSON SChema is valid
"""
import pytest
from src.contents.apiconstanrs import url_create_token, url_create_booking, url_update_delete_booking
from src.helpers.api_wrapper import post_request , put_data, delete_request
from src.helpers.common_verify import *
from src.helpers.payload_manager import payload_create_booking, payload_create_token, patch_update
from src.helpers.utils import common_headers, token_headers


class TestIntegration(object):

    @pytest.fixture()
    def test_create_token_tc01(self):
        response = post_request(url_create_token(), header=common_headers(), auth=None,
                            payload=payload_create_token(), in_json=False)
        assert response.status_code== 200
        token = response.json()["token"]
        print("your token "+ str(token))
        return token

    @pytest.fixture()
    def test_create_booking_tc02(self):
        response = post_request(url_create_booking(), header=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_code(response,200)
        verify_key(response.json()["bookingid"])
        booking_id = response.json()["bookingid"]
        print("it is your booking id--> "+ str(booking_id))
        return booking_id


    def test_update_booking_tc03(self,test_create_token_tc01, test_create_booking_tc02):
        response = put_data(url_update_delete_booking(test_create_booking_tc02),
                                header=token_headers(test_create_token_tc01), auth=None,
                                payload=patch_update(), in_json=False)
        verify_http_code(response,200)
        print(response.status_code)
        print(response.json())
        updated_name = response.json()["firstname"]
        print("This is your updated_name --> "+ updated_name)


    def test_delete_booking_tc04(self,test_create_token_tc01, test_create_booking_tc02):

        response = delete_request(url_update_delete_booking(test_create_booking_tc02),auth= None,
                                  header= token_headers(test_create_token_tc01),
                                  in_json=False)
        verify_http_code(response,201)
        print(response.status_code)
        print("deleted your id "+ str(self.test_create_booking_tc02))

    # calling required function by using import ( folder -->file -> function )
    # calling functions are URL, headers, auth, payload
    # pass the dependency-function as a parameter in main function


    # def test_create_booking_tc02(self):
    #     assert True == False
    #
    #
    # def test_create_booking_tc03(self):
    #     assert True == True


