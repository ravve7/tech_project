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

#
# from datetime import datetime
# from dateutil import tz
# import dateutil.parser
# # METHOD 1: Hardcode zones:
# format = '%Y-%m-%dT%H:%M:%S%z'
# datestring = '2019-07-29T15:12:45-02:00'
# d = dateutil.parser.parse(datestring) # python 2.7
# d = d.replace() - d.utcoffset()
# print(d)