import json
import csv
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
employ_data = open('EmployData.csv', 'w')
csvwriter = csv.writer(employ_data)
count = 0
with open('/home/manoj/Desktop/python/Ramya_mam_17-06-2018/OnePlus.json', 'r') as f:
    for i in f.readlines():
        #line = f.readlines() # read only the first tweet/line
	tweet = json.loads(i) # load it as Python dict
	emp = json.dumps(tweet, indent=4) # pretty-print
	if count == 0:
	    header = tweet.keys()
            csvwriter.writerow(header)
            count += 1
        csvwriter.writerow(tweet.values())
employ_data.close()
