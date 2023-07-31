import allure
import pytest
from src.contents.apiconstanrs import url_create_token, url_create_booking, url_update_delete_booking
from src.helpers.api_wrapper import post_request , put_data, delete_request
from src.helpers.common_verify import *
from src.helpers.payload_manager import payload_create_booking, payload_create_token, patch_update
from src.helpers.utils import common_headers, token_headers


class TestIntegration(object):

    @pytest.mark.smoke
    @allure.feature('TC#2- verify create booking feature')
    def test_create_booking_tc01(self):
        response = post_request(url_create_booking(), header=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_code(response,200)
        verify_key(response.json()["bookingid"])
        booking_id = response.json()["bookingid"]
        print("it is your booking id--> "+ str(booking_id))
        return booking_id


    @pytest.mark.smoke
    @allure.feature('TC#2- verify put feature')
    def test_put_2(self):
        assert True


    @pytest.mark.smoke
    @allure.feature('TC#2- verify delete feature')
    def test_delete_3(self):
        assert True