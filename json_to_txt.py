# -*- coding: utf-8 -*-
import json


with open("data_file.json", "r", encoding='utf8') as read_file:
    data = json.load(read_file)

with open("Podslushano_v_T.txt", "a", encoding="utf8") as results:
    for i in data["items"]:
        if i["text"]:
            try:
                results.write(i["text"])
                results.write('\n'*5)
            except:
                pass
