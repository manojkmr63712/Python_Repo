import json
import csv
import pandas as pd
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def load_json_multiple(segments):
    chunk = ""
    for segment in segments:
        chunk += segment
        try:
	    yield json.loads(chunk)
            chunk = ""
        except ValueError:
            pass

with open('/home/manoj/Desktop/python/Ramya_mam_17-06-2018/OnePlus.json', 'r') as f:
    for i in load_json_multiple(f):
	print i
