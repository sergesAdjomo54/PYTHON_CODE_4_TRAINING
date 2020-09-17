# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:22:13 2020

@author: james
"""


class SortedSet:
    
    def __init__(self, items=None):
        self._items = sorted(items) if items is not None else []