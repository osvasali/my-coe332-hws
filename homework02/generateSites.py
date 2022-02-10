import json
from random import seed
import random

def composition(): #sets meteorite composition
    list = ["stony", "iron", "stony-iron"]
    compo = random.choice(list)
    return compo

def latitude(): #sets meteorite latitude
    lat =  round( random.uniform(16.0, 18.0), 1)
    return lat

def longitude(): #sets meteorite longitude
    longi = round( random.uniform(82.0, 84.0), 1)
    return longi

meteorite_data = {}
meteorite_data['sites'] = []
for i in range(1,6):
    meteorite_data['sites'].append( { 'site_id': i, 'latitude' : latitude(), 'longitude' : longitude(), 'composition' :  composition()} )

with open('meteorite_data.json', 'w')as out:
    json.dump(meteorite_data, out, indent=2)
