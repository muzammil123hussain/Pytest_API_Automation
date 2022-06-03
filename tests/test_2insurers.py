import requests
from assertpy.assertpy import assert_that
import config
from data import expected_responses

def test_get_one_insurer():
    url = f'{config.BASE_URI}/sb/api/insurers/1'
    response = requests.get(url=url, headers=config.headers)
    # assert_that(response.json()).is_equal_to(expected_responses.insurer_expected_response)
    assert_that(response.status_code).is_equal_to(200)

def test_get_all_insurers():
    url = f'{config.BASE_URI}/sb/api/insurers'
    response = requests.get(url=url, headers=config.headers)
    assert_that(response.json()).contains_key("results")
    assert_that(response.status_code).is_equal_to(200)