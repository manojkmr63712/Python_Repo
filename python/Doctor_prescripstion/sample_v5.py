import string
from random import *
import random
import csv
import time
import uuid
import json
class Data():
    """docstring for Data"""
    def datagen(self):
	file = open('csvjson.json','r')
	data = json.load(file)
	file.close()
	#rawdata = random.choice(data)
	for raw in range(1,100):
	    rawdata = random.choice(data)
	    Timestamp = int(time.time())
	    sess = uuid.uuid4()
	    Session_id = str(sess)
	    min_char = 2
	    max_char = 4
	    allchar = string.digits
	    strdoctor = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
	    Doctor_Name = (rawdata['Doctor-Name'])
	    Doctor_ID = Doctor_Name[3:-3]+strdoctor
	    pallchar = string.digits
	    strpatient = "".join(choice(pallchar) for x in range(randint(min_char, max_char)))
	    Patient_Name = (rawdata['Patient-Name'])
	    Patient_ID = Patient_Name[3:-3]+strpatient
	    data = {"timestamp":Timestamp,
	    	"session_id":Session_id,
		"Doctor":{"Doctor-ID":Doctor_ID,"Doctor-Name":(rawdata['Doctor-Name']),"Surgery-Name":(rawdata['Surgery-Name'])},
		"Patient":{"Patient-ID":Patient_ID,"Patient-Name":(rawdata['Patient-Name']),"Patient-Detail":{"Smoking":(rawdata['Smoke']),"Alcoholic":(rawdata['Alcoholic']),"Age":(rawdata['Age']),"Disablity_Person":(rawdata['Disablity Person'])},"Patient-Treatment":{"Patient-History":(rawdata['History']),"Treatment-Name":(rawdata['Treatment Name']),"Drug-Name":(rawdata['Drug-Name']),"Dosage":(rawdata['Dosage']),"Refill":(rawdata['Refill']),"DoctorsNote":(rawdata['DoctorsNote'])},
		"Rx-Number":(rawdata['Rx Number']),"Rx-Expricy":(rawdata['RX Expricy']),"Dosing-Type":(rawdata['Dosing Type'])}
	        }
	    jsonData = json.dumps(data)
	    print(jsonData)
fidata = Data()
fidata.datagen()
