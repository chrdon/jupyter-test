#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 21:33:36 2017

@author: donner
"""

from lxml import html
import requests
import pandas as pd
import numpy as np

df = pd.read_csv('S+_Webseiten.csv', skiprows=6, usecols=[0],  sep=',',skipinitialspace=True)


#%%
url='http://www.xn--schlerpraktikum-1vb.de' + '/praktikumsplatz/mercur/15372'

page = requests.get(url)
tree = html.fromstring(page.content)

location = tree.xpath('//span[@class="location ellipsis"]/text()')
sector = tree.xpath('//span[@class="sector ellipsis"]/text()')
organization = tree.xpath('//span[@class="organization ellipsis"]/text()')
adress = tree.xpath('//div[@class="single_post_new_adresse_2"]//p/text()')
adress = list(map(str.strip, adress))
titel = tree.xpath('//h1[@class="title hyphenate"]/text()')
description = tree.xpath('//p[@class="description hyphenate"]/text()')


