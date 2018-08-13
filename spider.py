#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests as req
res = req.get("http://esf.cd.fang.com/house-a016418/")
from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text,"html.parser")
#print(soup.getText)
houses = soup.select(".shop_list.shop_list_4 dl") #shop_list
print("houses len:",len(houses))
#def getHouseInfo():
    #未完待续
domain = "http://esf.cd.fang.com"
for house in houses:
    try:
        print(domain+house.select(".floatl a")[0]['href'])
        #getHouseInfo(domain+house.select(". title a")[0]['href'])
    except Exception as e:
        print("------------->",e)

