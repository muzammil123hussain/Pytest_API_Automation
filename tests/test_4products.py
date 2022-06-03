import requests
from assertpy.assertpy import assert_that
import config

def test_get_one_product():
    products=[2,3]
    for product in products:
        url = f'{config.BASE_URI}/sb/api/products/{product}'
        response = requests.get(url=url, headers=config.headers)
        assert_that(response.status_code).is_equal_to(200)

def test_get_all_product():
    url = f'{config.BASE_URI}/sb/api/products/'
    response = requests.get(url=url, headers=config.headers)
    assert_that(response.json()).contains_key("results")
    assert_that(response.status_code).is_equal_to(200)