import string
from random import *
import csv
import time
import uuid
import json
class Data():
	"""docstring for Data"""
	def datagen(self):
		with open('datatemplate.csv','r') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',')
			next(spamreader, None)
			for row in spamreader:
				min_char = 2
				max_char = 4
				allchar = string.digits
				strpatient = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
				Timestamp = int(time.time())
				Session_id = uuid.uuid4()
				sess = str(Session_id)
				Doctor_Name = (row[4])
				Doctor_name = Doctor_Name[2:-2]
				Doctor_ID = Doctor_name + strpatient
				Surgery_Name = (row[5])
				Patient_ID = (row[6])
				Patient_Name = (row[7])
				Smoking = (row[13])
				Alcoholic = (row[14])
				Age = (row[16])
				Disablity_Person = (row[17])
				Patient_History = (row[15])
				Treatment_Name = (row[8])
				Drug_Name = (row[9])
				Dosage = (row[10])
				Refill = (row[11])
				DoctorsNote = (row[12])
				Rx_Number = (row[18])
				Rx_Expricy = (row[19])
				Dosing_Type = (row[20])
				print(str(Timestamp)+" "+str(sess)+" "+str(Doctor_ID)+" "+str(Doctor_Name))
				time.sleep(3)
fidata = Data()
fidata.datagen()