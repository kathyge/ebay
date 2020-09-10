# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:32:53 2020

@author: Katie
"""


import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Sellers Ratting':95, 'Starting Bid':200, 'Mumber of Bidders':4})

print(r.json())