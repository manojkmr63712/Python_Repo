import csv
import time
import uuid
import json
from kafka import KafkaProducer
class Data():
	"""docstring for Data"""
	def datagen(self):
		producer = KafkaProducer(bootstrap_servers='localhost:9092')
		try:
			with open('datatemplate.csv','r') as csvfile:
				spamreader = csv.reader(csvfile, delimiter=',')
				next(spamreader, None)
				for row in spamreader:
					Timestamp = int(time.time())
					Session_id = uuid.uuid4()
					sess = str(Session_id)
					data = {"timestamp":Timestamp,
					"session_id":sess,
					"Doctor":{"Doctor-ID":(row[3]),"Doctor-Name":(row[4]),"Surgery-Name":(row[5])},
					"Patient":{"Patient-ID":(row[6]),"Patient-Name":(row[7]),"Patient-Detail":{"Smoking":(row[13]),"Alcoholic":(row[14]),"Age":(row[16]),"Disablity_Person":(row[17])},"Patient-Treatment":{"Patient-History":(row[15]),"Treatment-Name":(row[8]),"Drug-Name":(row[9]),"Dosage":(row[10]),"Refill":(row[11]),"DoctorsNote":(row[12])},
					"Rx-Number":(row[18]),"Rx-Expricy":(row[19]),"Dosing-Type":(row[20])}
					}
					jsonData = json.dumps(data)
					producer.send('test', jsonData)
					print(jsonData)
					time.sleep(3)
				producer.flush()
		except IOError:
			producer.flush()
			print('An error occurred trying to read the file.')
		except ValueError:
			producer.flush()
			print('Non-numeric data found in the file.')
		except ImportError:
			producer.flush()
			print "NO module found"
		except EOFError:
			producer.flush()
			print('Why did you do an EOF on me?')
		except KeyboardInterrupt:
			producer.flush()
			print('End of Operation')
		except:
			producer.flush()
			print('An error occurred.')
fidata = Data()
fidata.datagen()