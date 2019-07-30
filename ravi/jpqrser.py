import requests
import json
from pytz import utc
def all_data():
    response = requests.get('http://127.0.0.1:8000/api/inventory_api/')
    data = response.json()
    myDict = dict()
    for each in data:
        name=each['products']['product_name']
        date=each['date']
        count = each['inventory_level']
        myDict.setdefault(name, []).append([date,count])
    return myDict
