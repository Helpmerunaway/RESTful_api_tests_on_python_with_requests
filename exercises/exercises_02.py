import pytest
import requests

"""
Exercise 2.1
# Create a test data object test_data_zip
# with three lines / test cases:
# country code - zip code - place
#           us -    90210 - Beverly Hills
#           it -    50123 - Firenze
#           ca -      Y1A - Whitehorse
"""

test_data_zip = [
    ('us', '90210', "Beverly Hills"),
    ('it', '50123', "Firenze"),
    ('ca', 'Y1A', "Whitehorse")
]

"""
# Exercise 2.2
# Write a parameterized test that retrieves user data using
# a GET call to http://api.zippopotam.us/<country_code>/<zip_code>
# and checks that the values for the 'place name' elements correspond
# to those that are specified in the test data object
"""


@pytest.mark.parametrize("country_code, zip_code, expected_place", test_data_zip)
def test_get_location_data_check_place_name(country_code, zip_code, expected_place):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body['places'][0]["place name"] == expected_place