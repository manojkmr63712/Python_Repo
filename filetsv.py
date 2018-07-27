#!/usr/bin/python

import csv
with open('/home/manoj/Documents/postresql/migration.tsv',)as fd:
    rd = csv.reader(fd,delimiter="\t")
    header_data = next(rd)
    da_data = []
    heade_data=1+len(header_data)
    #next(rd,None)
    for row in rd:
	for i in range(1, heade_data):
	    #print(row[i])
	    da_data.append(row[i])
	head_data = ', '.join('"{0}"'.format(w) for w in header_data)
	da1_data = ', '.join('"{0}"'.format(w) for w in da_data)
	print(row[0],head_data,da1_data)
	del da_data[:]
    del da_data[:]
