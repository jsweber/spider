# -*- coding: utf-8 -*-
__author__ = 'du'

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#print(os.path.abspath(__file__))#/Users/higgs/Documents/higgs/spider/renting/renting/main.py
execute(["scrapy", "crawl", "lianjia"])
