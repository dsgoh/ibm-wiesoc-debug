from elasticsearch import Elasticsearch
import time, datetime
import urllib.request
import json

# import local sources
import elasticWorker

es = Elasticsearch(
    cloud_id="ES-CLOUD-ID",
    http_auth=("ES-USER", "ES-PASS"),
)

def COVIDSafeBusinesses_metadata(timestamp, Business_reported_name, Business_reported_industry,	Business_reported_address, Business_reported_street_address, Business_reported_suburb, Business_reported_state, Business_reported_country, Business_reported_postcode, Business_standardised_address, Business_standardised_street_address, Business_standardised_Suburb, Business_standardised_State, Business_standardised_Postcode, Longitude, Latitude):
    metadata = {
        "timestamp" : timestamp.isoformat(),
        "Business_reported_name" : Business_reported_name,
        "Business_reported_industry" : Business_reported_industry,
        "Business_reported_address" : Business_reported_address,	
        "Business_reported_street_address" : Business_reported_street_address,    
        "Business_reported_suburb" : Business_reported_suburb,
        "Business_reported_state" :	Business_reported_state,
        "Business_reported_country" : Business_reported_country,
        "Business_reported_postcode" : Business_reported_postcode,
        "Business_standardised_address" : Business_standardised_address,
        "Business_standardised_street_address" : Business_standardised_street_address,
        "Business_standardised_Suburb" : Business_standardised_Suburb,	
        "Business_standardised_State" : Business_standardised_State,	
        "Business_standardised_Postcode" : Business_standardised_Postcode,
        "Longitude" : Longitude,	
        "Latitude" : Latitude
    }
    print(metadata)
    return metadata

indexCOVIDSafeBusinesses = "datansw-covidsafe-businesses-indexv1.0"

if __name__ == "__main__":
    with urllib.request.urlopen('https://data.nsw.gov.au/data/api/3/action/datastore_search?resource_id=4a26e0f0-71e1-43bb-96a8-e1434bbce9d8') as url:
        dataJSON = json.load(url) # dataJSON is a nested dict
        for business in list(dataJSON["result"]["records"]):
            COVIDSafeBusinesses_metadata(**{'timestamp': datetime.datetime.now(), **business})

    time.sleep(1)
    '''
    while True:
        #taxi_elasticWorker.log_index(es, index, m)
        time.sleep(1)
    '''
