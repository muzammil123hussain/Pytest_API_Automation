import requests
from assertpy.assertpy import assert_that
import config
from data import expected_responses

def test_get_one_bussiness_type():
    url = f'{config.BASE_URI}/sb/api/business-types/1'
    response = requests.get(url=url, headers=config.headers)
    assert_that(response.status_code).is_equal_to(200)

def test_get_all_bussiness_type():
    url = f'{config.BASE_URI}/sb/api/business-types'
    response = requests.get(url=url, headers=config.headers)
    assert_that(response.json()).contains_key("results")
    assert_that(response.status_code).is_equal_to(200)