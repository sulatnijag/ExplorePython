#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 23:26:42 2019

@author: jag
"""

import csv
import pprint


items = []
bids = []
heartbeat = []

pp = pprint.PrettyPrinter(indent=4)


#Read Input File
with open('input.txt') as csv_file:
    data = csv.reader(csv_file, delimiter='|')
    for row in data:
        if len(row) > 1:
            row_type = row[2]
            if row_type == 'SELL':
                items.append(row)
            elif row_type == 'BID':
                    bids.append(row)
            else:
                print("Unexpected row type")
                
pp.pprint(items)
pp.pprint(bids)