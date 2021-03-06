import googlemaps
from datetime import datetime

GOOGLEMAPS_KEY = 'API KEY HERE'

gmaps = googlemaps.Client(key=GOOGLEMAPS_KEY)

def queryVenue(input):
    """
    Use googlemaps to query a location with a query string
    
    Returns the formal address of the location as a string
    """
    place_id = gmaps.find_place(input=input, input_type="textquery")
    place = gmaps.place(place_id=place_id['candidates'][0]['place_id'])
    return place['result']


def queryRoute(origin, destination, departure_time=None, arrival_time=None):
    """
    Use googlemaps to query route from origin to destination
    """
    route = gmaps.directions(origin=origin, destination=destination, departure_time=departure_time, arrival_time=arrival_time, mode="transit")
    return route


# if __name__ == "__main__":
    # print(queryVenue("Mcdonalds George St Sydney"))

#     # Geocoding an address
#     geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

#     # Look up an address with reverse geocoding
#     reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

#     # Request directions via public transit
#     now = datetime.now()
#     directions_result = gmaps.directions("Sydney Town Hall",
#                                         "Parramatta, NSW",
#                                         mode="transit",
#                                         departure_time=now)
#     print(geocode_result)
#     print(reverse_geocode_result)
#     print(directions_result)