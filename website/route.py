import pandas # pip install
import requests
from io import StringIO
import maps

def getClosestStation(query):
    """
    Gets closest station to our long lat position and returns string of station name
    """
    return maps.queryVenue("train stations near " + query).partition(" ")[0] # get just name of station


def queryROAM(station):
    """
    Query the Rail Opal Assignment Model provided by Transport for NSW and returns an occupancy status
    """
    # requires login
    # response = requests.request("GET", "https://tfnsw-prod-opendata-tpa.s3-ap-southeast-2.amazonaws.com/ROAM/2020-10/ROAM_20201009.txt")
    # data = pandas.read_csv(StringIO(response.text))
    # print(data)

    data = 0
    with open("ROAM.csv", "r") as roam:
        for train in roam:
            if train.startswith(station):
                data = (train[::-1].partition("-")[0])[::-1] # reverse string to get info at end of string
                break
    return data

if __name__ == "__main__":
    station = getClosestStation("Belfield")
    print(queryROAM(station))