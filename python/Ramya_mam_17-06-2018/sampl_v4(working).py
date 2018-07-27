import json
import csv
import pandas as pd
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
with open('/home/manoj/Desktop/python/Ramya_mam_17-06-2018/apple (copy).json', 'r') as f:
    newDF = pd.DataFrame() 
    for i in f.readlines():
        tweet = json.loads(i) # load it as Python dict
	df = pd.io.json.json_normalize(tweet)
	newDF = newDF.append(df, ignore_index = True)
    newDF.to_csv('sampl_v4_apple.csv', sep=',', encoding='utf-8')
