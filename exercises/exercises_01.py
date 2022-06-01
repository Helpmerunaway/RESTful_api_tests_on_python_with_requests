import requests

response = requests.get("http://api.zippopotam.us/us/90210")
response_body = response.json()

"""
Exercise 1.1
Perform a GET request to http://api.zippopotam.us/us/90210
Check that the response status code equals 200
"""


def test_get_us_90210_response_status_code_200():
    assert response.status_code == 200


"""
Exercise 1.2
Perform a GET request to http://api.zippopotam.us/us/90210
Check that the value of the response header 'Content-Type' equals 'application/json'
"""


def test_get_us_90210_response_header_content_type_is_json():
    assert response.headers["Content-Type"] == 'application/json; charset=UTF-8'


"""
Exercise 1.3
Perform a GET request to http://api.zippopotam.us/us/90210
Check that the response body element 'country' has a value equal to 'United States'
"""


def test_us_90210_response_body_element_country_is_united_states():
    assert response_body["country"] == "United States"


"""
Exercise 1.4
Perform a GET request to http://api.zippopotam.us/us/90210
Check that the first 'place name' element in the list of places
has a value equal to 'Beverly Hills'
"""

def test_us_90210_response_place_name_element_equal_beverly_hills():
    assert response_body["places"][0]["place name"] == "Beverly Hills"


"""
# Exercise 1.5
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response body element 'places' has an array
# value with a length of 1 (i.e., there's one place that corresponds
# to the US zip code 90210)
"""


def test_us_90210_response_places_element_equal_():
    assert len(response_body["places"]) == 1