import pandas as pd
import json

resp = open('/home/manoj/Desktop/python/Ramya_mam_17-06-2018/OnePlus.json').read()
data = pd.read_json(resp)
msgs = pd.io.json.json_normalize(data)
print msgs
