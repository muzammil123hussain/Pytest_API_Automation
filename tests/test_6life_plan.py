import requests
from assertpy.assertpy import assert_that
import config
import pytest
from data import payloads


pytest.life_plan_id = None

def test_create_life_plan():
    url = f"{config.BASE_URI}/sb/api/plans/life/"
    payload = payloads.create_life_plan_payload()
    response = requests.post(url=url, data=payload, headers=config.headers)

    pytest.life_plan_id = response.json()['data']['id']
    assert_that(response.status_code).is_equal_to(201)

def test_get_one_life_plan():
    url = f'{config.BASE_URI}/sb/api/plans/life/{pytest.life_plan_id}?populate_fields=yes'
    response = requests.get(url=url, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)

def test_update_life_plan():
    url = f"{config.BASE_URI}/sb/api/plans/life/{pytest.life_plan_id}"
    payload = payloads.update_life_plan_payload()    
    response = requests.put(url=url, data=payload, headers=config.headers)
    assert_that(response.status_code).is_equal_to(201)

def test_get_all_life_plan():
    url = f'{config.BASE_URI}/sb/api/plans/life?populate_fields=yes&comman_sep_ids1=3,2'
    response = requests.get(url=url, headers=config.headers)
    assert_that(response.json()).contains_key("results")
    assert_that(response.status_code).is_equal_to(200)