# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:15:59 2020

@author: kylel
"""

import requests
import json

respond = requests.get("https://www.dcard.tw/service/api/v2/forums/pet/posts?popular=true&limit=30&before=233450431")
JsonData = json.loads(respond.text)


count = 1
for  data in JsonData:
    Data = {"Title":data['title'],
        "Topic":data['topics'],
        "Gender":data['gender'],
        "school":data['school']}
    with open("dcard_pet_40info.json","a",encoding="utf-8") as file:
        json.dump(Data, file,ensure_ascii=False)






                      