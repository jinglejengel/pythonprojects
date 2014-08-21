import requests
import json

products_url = 'https://api.uber.com/v1/products'

parameters = {
    'server_token': '',
    'latitude': 29.437730,
    'longitude': -98.478785,
}

products = requests.get(products_url, params=parameters)

print "The available products in your area are: "
print json.dumps(products.json(), indent=4)

print

time_url = 'https://api.uber.com/v1/estimates/time'

parameters = {
    'server_token': '',
    'start_latitude': 29.437730,
    'start_longitude': -98.478785,
}

timing = requests.get(time_url, params=parameters)

print "The ETA for the closest ride is: "
print json.dumps(timing.json(),indent=4)

print

price_url = 'https://api.uber.com/v1/estimates/price'

parameters = {
    'server_token': '',
    'start_latitude': 29.437730,
    'start_longitude': -98.478785,
    'end_latitude': 29.508241,
    'end_longitude': -98.394049
}

price = requests.get(price_url, params=parameters)

print "The estimated cost to work is: "
print json.dumps(price.json(), indent=4)

print
