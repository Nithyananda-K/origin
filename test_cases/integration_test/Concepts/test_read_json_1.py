import os
import pytest
from dotenv import load_dotenv
import json

def test_beta_url():
    with open("beta.json","r" ) as beta:
        data= json.load(beta)
        print(data)
    return

def tes_get_url(test_beta_url):
    print(test_beta_url["url"])