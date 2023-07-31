# HTTP Status Code

def verify_http_code(response_data, expected_data):
    # print(response_data.status_code)
    assert response_data.status_code == expected_data

# Any key, should not be null, of empty

def verify_key(key):
    assert key != 0, "key is non Empty : " + key
    assert key > 0, "key should be greater than zero"

