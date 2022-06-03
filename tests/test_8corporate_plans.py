from urllib import response
import pytest
import requests
from assertpy.assertpy import assert_that
from json import dumps
import config
from data import payloads

pytest.corp_plan_id = None

def test_add_health_plan_in_corporate():
    url = f"{config.BASE_URI}/sb/api/corporates/plans/"
    payload = payloads.add_health_plan_in_corporate_payload()

    response = requests.post(url=url, data=payload, headers=config.headers)
    assert_that(response.status_code).is_equal_to(201)

def test_add_lifes_plan_in_corporate():
    url = f"{config.BASE_URI}/sb/api/corporates/plans/"
    payload = payloads.add_life_plan_in_corporate_payload()

    response = requests.post(url=url, data=payload, headers=config.headers)
    assert_that(response.status_code).is_equal_to(201)

def test_aggregate_corporate():
    url = f"{config.BASE_URI}/sb/api/corporates/plans/aggregate?corporate_id={pytest.corp_id}"
    response = requests.get(url=url, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).contains_key("results")


def test_corporate_all_plans():
    url = f"{config.BASE_URI}/sb/api/corporates/plans?corporate_id={pytest.corp_id}"
    response = requests.get(url=url, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)
    response_json = response.json()
    pytest.corp_plan_id = response_json['results'][0]['id']
    assert_that(response_json).contains_key("results")

def test_get_corporate_one_plan():
    url = f"{config.BASE_URI}/sb/api/corporates/plans/{pytest.corp_plan_id}"
    response = requests.get(url=url, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)
