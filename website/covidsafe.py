import urllib.request
from difflib import SequenceMatcher
import json

def checkCovidSafe(address):
    # name = venue["name"]
    # a = venue["address_components"]
    # street_address = a[0]["short_name"]
    # suburb = a[1]["short_name"]
    # postcode = a[4]["short_name"]
    # print(name)
    address = address.split(",")
    
    # address1 = " ".join(address[0].split(" ")[:-1])
    address1 = address[0].upper()

    address2 = address[1].strip()
    suburb = address2.split(" ")[0]

    address2 = address2.upper()
    
    with urllib.request.urlopen(f'https://data.nsw.gov.au/data/api/3/action/datastore_search?resource_id=4a26e0f0-71e1-43bb-96a8-e1434bbce9d8&q={suburb}') as url:
            dataJSON = json.load(url) # dataJSON is a nested dict
            businesses = list(dataJSON["result"]["records"])
            # print(businesses[0])

            for business in businesses:
                # if not business["Business_standardised_street_address"]: continue
                # if not business["Business_standardised_Suburb"]: continue
                # if not business["Business_standardised_State"]: continue
                # if not business["Business_standardised_Postcode"]: continue

                address1_b = business["Business_reported_street_address"].upper()
                address2_b = f'{business["Business_reported_suburb"]} {business["Business_reported_state"]} {business["Business_reported_postcode"]}'.upper()
                # if (name.upper() == business["Business_reported_name"].upper() and
                if (similar(address1, address1_b) and similar(address2, address2_b)):
                    return True

    return False



def similar(a, b):
    return SequenceMatcher(None, a, b).ratio() > 0.75

print(checkCovidSafe("2/309 Anzac Parade, Kingsford NSW 2032"))