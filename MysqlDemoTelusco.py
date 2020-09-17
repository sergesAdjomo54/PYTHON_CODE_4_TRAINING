# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 09:33:41 2020

@author: james
"""

import sqlite3


conn = sqlite3.connect(host="localhost", user="root", passwd="")
cur = conn.cursor()
req = cur.execute("show database")
for row in req:
   print(row)

