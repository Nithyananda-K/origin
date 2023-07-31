import os
import pytest
from dotenv import load_dotenv
import json


@pytest.fixture
def test_beta_url():
    # test_beta_url()
    load_dotenv()
    file_name = os.getenv("load_env")
    print(file_name)
    with open(file_name,"r" ) as beta:
        data= json.load(beta)
    # print(data["url"])
    return data

def test_get_url(test_beta_url):
    print(test_beta_url["url"])

