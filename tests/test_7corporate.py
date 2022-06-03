import pytest
import requests
from assertpy.assertpy import assert_that
from json import dumps
import config
from data import payloads
import time


pytest.corp_id = None
pytest.corp_code = None

def test_create_corporate():
    url = f"{config.BASE_URI}/sb/api/corporates/"

    payload = payloads.create_corporate_payload()

    response = requests.post(url=url, data=payload, headers=config.headers)

    pytest.corp_id = response.json()['data']['id']
    pytest.corp_code = response.json()['data']['code']

    assert_that(response.status_code).is_equal_to(201)

def test_bulk_create_corporate():

    url = f'{config.BASE_URI}/sb/api/corporates/'

    payload = payloads.create_bulk_corporate_payload()

    response = requests.post(url=url, data=payload, headers=config.headers)
    assert_that(response.status_code).is_equal_to(201)

def test_get_one_corporate():
    url = f'{config.BASE_URI}/sb/api/corporates/{pytest.corp_id}'
    response = requests.get(url, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)

def test_update_corporate():
    url = f"{config.BASE_URI}/sb/api/corporates/{pytest.corp_id}"
    payload = dumps({
        "address": "Karachi, Sindh, Pakistan"
    })
    response = requests.put(url=url, data=payload, headers=config.headers)

    assert_that(response.status_code).is_equal_to(201)

def test_get_corporate_list():
    url = f'{config.BASE_URI}/sb/api/corporates/'
    response = requests.get(url, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)

    