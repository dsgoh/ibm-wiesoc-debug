import urllib.request
import json
from datetime import date, timedelta
import maps

# gets number of covid cases notified in the venue's postcode in the last 14 days
# input googlemaps json object (like the covid safe business check function)
# returns int
def checkCovidLocation(venue):
    
    today = date.today()
    count_from = today - timedelta(days=14)

    postcode = getPostcode(venue)
    if postcode == "": return 0
    d = date.fromisoformat('2020-09-27')

    with urllib.request.urlopen(f'https://data.nsw.gov.au/data/api/3/action/datastore_search?resource_id=2776dbb8-f807-4fb2-b1ed-184a6fc2c8aa&q={postcode}') as url:
            dataJSON = json.load(url) # dataJSON is a nested dict
            cases = list(dataJSON["result"]["records"])

    count = 0
    for case in cases:
        d = date.fromisoformat(case["notification_date"])
        if d >= count_from:
            count += 1
        

    return count


# postcode from googlemaps json object
def getPostcode(venue):
    postcode = ""
    for c in venue["address_components"]:
        if "postal_code" in c["types"]:
            postcode = c["long_name"]
    return postcode



# v = maps.queryVenue("ruby massage")
# print(checkCovidLocation(v))