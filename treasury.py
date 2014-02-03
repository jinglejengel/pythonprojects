#!/usr/bing/env python
#
# Treasury data miner
# Description: Utilizing http://treasury.io and the python plug in, this script queries a remote SQL database
# and returns an array of JSON records which then imports to mongo using pymongo
#
# Requires pymongo and treasuryio from pip installer
#
# Written by Joe Engel

import treasuryio
import pymongo

db = pymongo.MongoClient().treasury

# Feel free to replace this SQL query with any from http://treasury.io
sql = 'SELECT "table", "date", "year_month", "year", "month", "day", "weekday", "is_total", "parent_item", "item", "item_raw", "close_today", "open_today", "open_mo", "open_fy", "url" FROM t3c WHERE ("date" > "2005-06-09");'

res = treasuryio.query(sql, format='dict')

for record in res:
        db.creditlimit.save(record)
