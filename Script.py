#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 20:13:11 2020

@author: Alok
"""


import sys
import json
import os

with open('./data.json') as f:
  data = json.load(f)

print(data)

for k,v in data['Dependencies'].items():
    try:
        s = 'pip3 install '+k+'=='+v
        os.system(s)
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
        
    finally:
        print("Succesfully installed "+k+v)
        
        
