from pprint import pprint
import pytest
import requests
from assertpy.assertpy import assert_that
import config
from data import payloads

pytest.access_token = None

def test_register_step_one():
    url = f"{config.BASE_URI}/sb/api/users/register/step-1/"
    payload = payloads.register_step_one_payload()
    response = requests.post(url=url, data=payload, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)

def test_register_step_two():
    url = f"{config.BASE_URI}/sb/api/users/register/"
    payload = payloads.register_step_two_payload()
    response = requests.post(url=url, data=payload, headers=config.headers)
    assert_that(response.status_code).is_equal_to(201)

def test_verify_otp():
    url = f"{config.BASE_URI}/sb/api/otp/verify/"
    payload = payloads.verify_otp_payload()
    response = requests.post(url=url, data=payload, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)

def test_login():
    url = f"{config.BASE_URI}/sb/api/token/"
    payload = payloads.login_payload()
    response = requests.post(url=url, data=payload, headers=config.headers)
    pytest.access_token = response.json()['access']
    assert_that(response.status_code).is_equal_to(200)

def test_generate_otp():
    url = f"{config.BASE_URI}/sb/api/otp/generate/"
    payload = payloads.generate_otp_payload()
    response = requests.post(url=url, data=payload, headers=config.headers)
    assert_that(response.status_code).is_equal_to(201)

def test_reset_password():
    url = f"{config.BASE_URI}/sb/api/users/reset_password/"
    payload = payloads.reset_password_payload()
    response = requests.post(url=url, data=payload, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)

def test_get_my_profile():
    test_login()
    url = f"{config.BASE_URI}/sb/api/profile/"
    headers = {
        'Authorization': f"Bearer {pytest.access_token}"
    }
    response = requests.get(url=url, headers=headers)
    assert_that(response.status_code).is_equal_to(200)

def test_update_my_profile():
    url = f"{config.BASE_URI}/sb/api/profile/"
    headers = {
        'Authorization': f"Bearer {pytest.access_token}",
        'Content-Type': 'application/json'
    }
    payload = payloads.update_profile()

    response = requests.put(url=url, data=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(200)

def test_get_my_plans():
    url = f"{config.BASE_URI}/sb/api/profile/plans"
    headers = {
        'Authorization': f"Bearer {pytest.access_token}"
    }
    response = requests.get(url=url, headers=headers)
    assert_that(response.status_code).is_equal_to(200)

def test_get_cities():
    url = f"{config.BASE_URI}/sb/api/cities/?insurer_id=1"
    headers = {
        'Authorization': f"Bearer {pytest.access_token}"
    }
    response = requests.get(url=url, headers=headers)
    assert_that(response.status_code).is_equal_to(200)

def test_get_hospitals():
    url = f"{config.BASE_URI}/sb/api/hospitals/?insurer_id=1"
    headers = {
        'Authorization': f"Bearer {pytest.access_token}"
    }
    response = requests.get(url=url, headers=headers)
    assert_that(response.status_code).is_equal_to(200)

def test_get_labs():
    url = f"{config.BASE_URI}/sb/api/labs/?insurer_id=1"
    headers = {
        'Authorization': f"Bearer {pytest.access_token}"
    }
    response = requests.get(url=url, headers=headers)
    assert_that(response.status_code).is_equal_to(200)

def test_get_day_care_surgeries():
    url = f"{config.BASE_URI}/sb/api/day-care-surgeries/?insurer_id=1"
    headers = {
        'Authorization': f"Bearer {pytest.access_token}"
    }
    response = requests.get(url=url, headers=headers)
    assert_that(response.status_code).is_equal_to(200)

def test_get_special_investigation_tests():
    url = f"{config.BASE_URI}/sb/api/special-investigation-tests/?insurer_id=1"
    headers = {
        'Authorization': f"Bearer {pytest.access_token}"
    }
    response = requests.get(url=url, headers=headers)
    assert_that(response.status_code).is_equal_to(200)

def test_reimbursement_claim():
    url = f"{config.BASE_URI}/sb/api/claims/reimbursement/"
    headers = {
        'Authorization': f"Bearer {pytest.access_token}"
    }
    payload = payloads.reimbursement()
    files = payloads.reimbursement_files()

    response = requests.post(url=url, data=payload, headers=headers, files=files)
    assert_that(response.status_code).is_equal_to(201)

def test_planned_surgery_prior_approval():
    url = f"{config.BASE_URI}/sb/api/claims/planned-surgery-prior-approval/"
    headers = {
        'Authorization': f"Bearer {pytest.access_token}"
    }
    payload = payloads.planned_surgery()
    files = payloads.planned_surgery_files()

    response = requests.post(url=url, data=payload, headers=headers, files=files)
    print(pytest.phone_no, pytest.password)
    assert_that(response.status_code).is_equal_to(201)
