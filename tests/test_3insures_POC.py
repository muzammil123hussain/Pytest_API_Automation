import requests
from assertpy.assertpy import assert_that
import config
import pytest
from data import payloads


pytest.insurer_poc_id = None

def test_create_insurer_poc():
    url = f"{config.BASE_URI}/sb/api/insurers/poc/"
    payload = payloads.create_insurer_poc_payload()
    response = requests.post(url=url, data=payload, headers=config.headers)
    pytest.insurer_poc_id = response.json()['data']['id']
    assert_that(response.status_code).is_equal_to(201)

def test_get_one_insurer_poc():
    url = f'{config.BASE_URI}/sb/api/insurers/poc/{pytest.insurer_poc_id}'
    response = requests.get(url=url, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)

def test_update_insurer_poc():
    url = f"{config.BASE_URI}/sb/api/insurers/poc/{pytest.insurer_poc_id}"
    payload = payloads.update_insurer_poc_payload()    
    response = requests.put(url=url, data=payload, headers=config.headers)
    assert_that(response.status_code).is_equal_to(201)

def test_delete_insurer_poc():
    url = f"{config.BASE_URI}/sb/api/insurers/poc/{pytest.insurer_poc_id}" 
    response = requests.delete(url=url, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)

def test_get_all_insurer_poc():
    url = f'{config.BASE_URI}/sb/api/insurers/poc/'
    response = requests.get(url=url, headers=config.headers)
    assert_that(response.json()).contains_key("results")
    assert_that(response.status_code).is_equal_to(200)