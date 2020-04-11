# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:45:07 2020

@author: kylel
"""

import requests

respond = requests.get("https://www.dcard.tw/service/api/v2/forums/pet/posts?popular=true&limit=30&before=233450431")
jsonData = respond.json()

for data in jsonData:
    count = 1
    title = data['title']
    for picture in data['media']:
        try:
            with open("images\\"+title + str(count)+".jpg","bw") as file:
                file.write(requests.get(picture['url']).content)
        except OSError:
                continue
        count += 1