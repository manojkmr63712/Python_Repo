import csv
import time
import uuid
import json
import random
class Data():
	"""docstring for Data"""
	def datagen(self):
		data = []
		with open('datatemplate.csv','r') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',')
			next(spamreader, None)
			for row in spamreader:
				data.append(row)
		for i in range(1,1000):
			rawdata = random.choice(data)
			print(rawdata)			
fidata = Data()
fidata.datagen()