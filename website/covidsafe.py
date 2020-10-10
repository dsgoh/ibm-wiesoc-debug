import urllib.request
import json

def checkCovidSafe(venue):
    # name = venue["name"]
    # a = venue["address_components"]
    # street_address = a[0]["short_name"]
    # suburb = a[1]["short_name"]
    # postcode = a[4]["short_name"]
    # print(name)
    print(venue["formatted_address"])
    address = venue["formatted_address"].split(",")
    address1 = address[0].upper()
    address2 = address[1].strip().upper()
    
    with urllib.request.urlopen('https://data.nsw.gov.au/data/api/3/action/datastore_search?resource_id=4a26e0f0-71e1-43bb-96a8-e1434bbce9d8') as url:
            dataJSON = json.load(url) # dataJSON is a nested dict
            businesses = list(dataJSON["result"]["records"])
            # print(businesses[0])

            for business in businesses:
                if not business["Business_standardised_street_address"]: continue
                if not business["Business_standardised_Suburb"]: continue
                if not business["Business_standardised_State"]: continue
                if not business["Business_standardised_Postcode"]: continue

                address1_b = business["Business_standardised_street_address"].upper()
                address2_b = f'{business["Business_standardised_Suburb"]} {business["Business_standardised_State"]} {business["Business_standardised_Postcode"]}'.upper()
                # if (name.upper() == business["Business_reported_name"].upper() and
                if ((address1 in address1_b or address1_b in address1) and
                    (address2 in address2_b or address2_b in address2)):
                    return True

    return False



# print(checkCovidSafe("Ben Hall Beau Thai", "99 Lachlan St", "FORBES", "2871"))