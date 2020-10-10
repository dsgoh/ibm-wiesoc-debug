from elasticsearch import Elasticsearch
import time, datetime

def log_index(es, indexIn, data):
    
    res = es.index(index=indexIn, body=data)
    print(res['result'])
