# import pandas # pip install
# import requests
# from io import StringIO
from datetime import datetime
import maps
import random

def getClosestStation(query):
    """
    Gets closest station to our long lat position and returns string of station name
    """
    return maps.queryVenue("train stations near " + query)['formatted_address'].partition(" ")[0] # get just name of station


def queryROAM(station, datetimein):
    """
    Query the Rail Opal Assignment Model provided by Transport for NSW and returns an occupancy status
    """
    # requires login
    # response = requests.request("GET", "https://tfnsw-prod-opendata-tpa.s3-ap-southeast-2.amazonaws.com/ROAM/2020-10/ROAM_20201009.txt")
    # data = pandas.read_csv(StringIO(response.text))
    # print(data)

    data = []
    with open("../ROAM.csv", "r") as roam:
        for train in roam:
            if train.startswith(station):
                val = train[::-1].partition("-")[0][::-1] # reverse string to get info at end of string
                data.append(val)
                break
    if (isinstance(data, str) or len(data) == 0):
        return 0
    return data[random.random() % len(data)]

if __name__ == "__main__":
    station = getClosestStation("Woolworths Parramatta")
    print(station)
    print(queryROAM(station, datetime.now()))