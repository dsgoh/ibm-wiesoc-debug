import datetime
import requests
import json

import maps

BESTTIME_KEY = 'API key from site'

def checkAuthorisation():
    """
    Checks the API key and returns details about it
    """
    payload = {}
    headers= {}
    response = requests.request("GET", 'https://BestTime.app/api/v1/keys/' + BESTTIME_KEY, headers=headers, data = payload)
    print(response.text.encode('utf8'))

def forecastVenue(queryString, time):
    """
    Query the venue. Makes a call to googlemaps API to get formal address
    """
    params = {
        'api_key_private': BESTTIME_KEY,
        'venue_name': queryString,
        'venue_address': maps.queryVenue(queryString)
    }
    response = requests.request("POST", 'https://besttime.app/api/v1/forecasts', params=params)
    data = json.loads(response.text)
    print(data)
    return data

# def extractJSON():

if __name__ == '__main__':
    forecastVenue("Mcdonalds George St Sydney", datetime.datetime.now())
