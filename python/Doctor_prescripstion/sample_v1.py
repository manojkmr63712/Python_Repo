import csv
import time
import uuid
import json
class Data():
	"""docstring for Data"""
	Timestamp = ''
	Session_id=''
	Doctor_ID=''
	Doctor_Name=''
	Surgery_Name=''
	Patient_ID=''
	Patient_Name=''
	Treatment_Name=''
	Drug_Name=''
	Dosage=''
	Refill=''
	DoctorsNote=''
	Smoke=''
	Alcoholic=''
	History=''
	Age=''
	Disablity_Person=''
	Rx_Number=''
	RX_Expricy=''
	Dosing_Type=''
	def datagen(self):
		Timestamp = int(time.time())
		Session_id = uuid.uuid4()
		sess = str(Session_id)
		data = {"timestamp":Timestamp,
				"session_id":sess,
				"Doctor":{"Doctor-ID":Doctor_ID,"Doctor-Name":Doctor_Name,"Surgery-Name":Surgery_Name},
				"Patient":{"Patient-ID":Patient_ID,"Patient-Name":Patient_Name},
				"Patient-Treatment":{"Patient-History":History,"Treatment-Name":Treatment_Name,"Drug-Name":Drug_Name,"Dosage":Dosage,"Refill":Refill,"DoctorsNote":DoctorsNote,
				"Rx-Number":Rx_Number,"Rx-Expricy":RX_Expricy,"Dosing-Type":Dosing_Type},
				"Patient-Detail":{"Smoking":Smoke,"Alcoholic":Alcoholic,"Age":Age,"Disablity_Person":Disablity_Person}}
		jsonData = json.dumps(data)
		print(jsonData)
		
fidata = Data()
with open('datatemplate.csv','r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	next(spamreader, None)
	for row in spamreader:
		Doctor_ID = (row[3])
		Doctor_Name = (row[4])
		Surgery_Name = (row[5])
		Patient_ID = (row[6])
		Patient_Name = (row[7])
		Treatment_Name = (row[8])
		Drug_Name = (row[9])
		Dosage = (row[10])
		Refill = (row[11])
		DoctorsNote = (row[12])
		Smoke = (row[13])
		Alcoholic = (row[14])
		History = (row[15])
		Age = (row[16])
		Disablity_Person = (row[17])
		Rx_Number = (row[18])
		RX_Expricy = (row[19])
		Dosing_Type = (row[20])
		Timestamp = int(time.time())
		Session_id = uuid.uuid4()
		sess = str(Session_id)
		data = {"timestamp":Timestamp,
			"session_id":sess,
			"Doctor":{"Doctor-ID":Doctor_ID,"Doctor-Name":Doctor_Name,"Surgery-Name":Surgery_Name},
			"Patient":{"Patient-ID":Patient_ID,"Patient-Name":Patient_Name},
			"Patient-Treatment":{"Patient-History":History,"Treatment-Name":Treatment_Name,"Drug-Name":Drug_Name,"Dosage":Dosage,"Refill":Refill,"DoctorsNote":DoctorsNote,
			"Rx-Number":Rx_Number,"Rx-Expricy":RX_Expricy,"Dosing-Type":Dosing_Type},
			"Patient-Detail":{"Smoking":Smoke,"Alcoholic":Alcoholic,"Age":Age,"Disablity_Person":Disablity_Person}}
		jsonData = json.dumps(data)
		print(jsonData)
		time.sleep(3)