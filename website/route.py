# import pandas # pip install
# import requests
# from io import StringIO
from datetime import datetime
import operator
import maps

def nearest(items, pivot):
    return min(items, key=lambda d: abs(datetime.strptime(d[0], '%b %d %Y %I:%M%p') - pivot))

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
                trainSplit = list(train.split("|"))
                dt = trainSplit[3]
                occ = trainSplit[-1].partition("-")[0]
    if (isinstance(data, str) or len(data) == 0):
        return 0
    return data[0][1]

if __name__ == "__main__":
    station = getClosestStation("Belfield")
    print(queryROAM(station, datetime.now()))