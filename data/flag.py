import requests


def fetch_flag(*country_name):
    """
    Fetches link flag from the API.
    """
    # fetch the first country in the list of countries
    country = country_name[0]
    api_url = 'https://restcountries.com/v3.1/name/{}'.format(country)
    response = requests.get(api_url)
    data = response.json()

    #return data
    for country in data:
        return country["flags"]["png"]



