import json
import csv
import pandas as pd
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
with open('/home/manoj/Desktop/python/Ramya_mam_17-06-2018/OnePlus.json', 'r') as f:
    for i in f.readlines():
        tweet = json.loads(i) # load it as Python dict
	df = pd.io.json.json_normalize(tweet)
    	print df
