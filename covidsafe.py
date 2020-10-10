import urllib.request
import json

def checkCovidSafe(name, street_address, suburb, postcode):
    with urllib.request.urlopen('https://data.nsw.gov.au/data/api/3/action/datastore_search?resource_id=4a26e0f0-71e1-43bb-96a8-e1434bbce9d8') as url:
            dataJSON = json.load(url) # dataJSON is a nested dict
            businesses = list(dataJSON["result"]["records"])
            # print(businesses[0])
            for business in businesses:
                if (name.upper() == business["Business_reported_name"].upper() and
                    street_address.upper() == business["Business_standardised_street_address"].upper() and
                    suburb.upper() == business["Business_standardised_Suburb"] and
                    postcode.upper() == business["Business_standardised_Postcode"]):
                    return True

    return False



print(checkCovidSafe("Ben Hall Beau Thai", "99 Lachlan St", "FORBES", "2871"))