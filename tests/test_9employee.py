import pytest
import requests
from assertpy.assertpy import assert_that
import config
from data import payloads

pytest.emp_id = None
pytest.emp_cnic = None

def test_create_employee():
    url = f"{config.BASE_URI}/sb/api/employees/"

    payload = payloads.create_employee_payload()

    response = requests.post(url=url, data=payload, headers=config.headers)
    pytest.emp_id = response.json()['data']['id']
    pytest.emp_cnic = response.json()['data']['cnic']
    pytest.corp_id = response.json()['data']['corporate']
    assert_that(response.status_code).is_equal_to(201)

def test_update_employee():
    url = f"{config.BASE_URI}/sb/api/employees/{pytest.emp_id}"
    payload = payloads.update_employee_payload()

    response = requests.put(url=url, data=payload, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)

def test_bulk_create_employee():
    url = f'{config.BASE_URI}/sb/api/employees/'

    payload = payloads.create_bulk_employee_payload()

    response = requests.post(url=url, data=payload, headers=config.headers)
    assert_that(response.status_code).is_equal_to(201)

def test_get_one_employee():
    url = f'{config.BASE_URI}/sb/api/employees/{pytest.emp_id}'

    response = requests.get(url, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)


def test_get_employee_list_against_corporate():
    url = f'{config.BASE_URI}/sb/api/employees/?corporate_id={pytest.corp_id}'

    response = requests.get(url, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)