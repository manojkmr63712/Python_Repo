import string
from random import *
import random
import time
import uuid
import json
from kafka import KafkaProducer
class Data():
    """docstring for Data"""
    def datagen(self):
	doct_name = ['Jagadeesh','Ramasamy','Karthick','Sirumugai','Arunkumar','Jagadeesh','Ramasamy','Karthick','Sirumugai','ManojKumar','SaiKumar','JeganKumar','SurenKumar','KiranKumar','AshwinKumar','SarinKumar','SomakKumar','NirmalKumar','SuryaKumar']
	surge_name = ['Heart','Nervous','Respiratory Diseases','Tuberculosis','Malignant and Other Tumours','Digestive Diseases','Diarrheal Diseases','Unintentional Injuries','Intentional Self Harm','Malaria','Bye-pass','Cataract surgery','Urethroplasty','Cosmetic Surgery','Arthoplasty','Inguinal hernia','Prostatectomy','Cholecystectomy','Appendectomy','Polypectomy']
        patint_name = ['Arvind','Naveen','Shanmugam','Muthu','Krishna','Gopi','Vijay','Dharma','Selva','Mani','Akash','Amar','Anoop','Ram','Ashwin','Raghav','Naren','Mark','Murali','Smith']
	tretmnt_name = ['Remove Blogs','Control of FIX','To Freeze the Breathing','Tuberculosis','Malignant and Other Tumours','Digestive Diseases','Diarrheal Diseases','Accident Injuries','Depression','Malaria','Preventive Heart-attack','Eye Blurredness','Urine Difficulty','Skin Allergies','Knee Join Replacement','Hernia Correction','Prostrate Gland Correction','Gallbladder Removal','Appendix Removal','Colon Growth Removal']
	drug_name = ['Lipitor','Campral EC.','Cefadroxil','Isoniazid','Carboplatin','Invertase','loperamide','ketoconazole','Prozac','Malarone','Bisoprolol','Aspirin','Flavoxate','Cetrizine','Aleve','Zantac','Uroxatral','Ursodial','Zosyn','Avastin']
	dosage =['80mg','50mg','100mg','60mg','10mg','5mg','75mg','8mg','4 mg','1mg']
	refill = [3,2,4,5,1]
	doctorsnote = ['Mini stoke','control of Fix','External Action in place','External Action in place','Regular oilment','Glucose to be in place','Glucose to be in place','Regular oilment','Patient should care','Regular oilment','Mild Attack','Eye Puffiness','High Uric Acid','Rashes and Itching in Skin','Knee Pain','Groin Pain','Urinary Incontinence','GallStones','Intestine Inflammation','Rectal Bleeding']
	smoke = ['yes','no']
	alcoholic = ['yes','no']
	history = ['yes','no']
	age = [61,60,55,59,70,45,64,45,50,40,34,47,30,27,36,25,48]
	disablity = ['yes','no']
	rxnum = ['RX829','RX546','RX980','RX670','RX679','RX879','RX780','RX456','RX345','RX567','RX780','RX860','RX777','RX989','RX575','RX333','RX423','RX921','RX543','RX199']
	rxexp = ['08/18','08/18','18/Dec','18/Dec','18/Dec','18/Dec','18/Dec','20/Dec','19/Nov','19/Nov','16/Sep','19/Oct','21/Nov','22/Dec','14/Aug','25/Dec','16/Oct','12/Sep','11/Aug','10/Jul']
	dosingtype = ['Twice in a Day','Thrice in a Day','Once in a Day']
	count = 0
	#producer = KafkaProducer(bootstrap_servers='localhost:9092')
	try:
	    while True:
		for raw in range(0,100000):
		    count += 1
		    Timestamp = int(time.time())
	            sess = uuid.uuid4()
	            Session_id = str(sess)
	            min_char = 2
	            max_char = 4
	            allchar = string.digits
	            strdoctor = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
	            Doctor_Name = random.choice(doct_name)
		    Doctor_ID = Doctor_Name[3:-3]+strdoctor
	            pallchar = string.digits
	            strpatient = "".join(choice(pallchar) for x in range(randint(min_char, max_char)))
	            Patient_Name = random.choice(patint_name)
	            Patient_ID = Patient_Name[3:-3]+strpatient
	            data = {"timestamp":Timestamp,
	    		"session_id":Session_id,
			"Doctor":{"Doctor-ID":Doctor_ID,"Doctor-Name":Doctor_Name,"Surgery-Name":random.choice(surge_name)},
			"Patient":{"Patient-ID":Patient_ID,"Patient-Name":Patient_Name,"Patient-Detail":{"Smoking":random.choice(smoke),"Alcoholic":random.choice(alcoholic),"Age":random.choice(age),"Disablity_Person":random.choice(disablity)},"Patient-Treatment":{"Patient-History":random.choice(history),"Treatment-Name":random.choice(tretmnt_name),"Drug-Name":random.choice(drug_name),"Dosage":random.choice(dosage),"Refill":random.choice(refill),"DoctorsNote":random.choice(doctorsnote)},
			"Rx-Number":random.choice(rxnum),"Rx-Expricy":random.choice(rxexp),"Dosing-Type":random.choice(dosingtype)}
	            }
	            jsonData = json.dumps(data)
		    #producer.send('test', jsonData)
	            print(jsonData)
		    print(count)
	    	time.sleep(5)
	except KeyboardInterrupt:
	    #producer.flush()
	    print('End of Operation')
fidata = Data()
fidata.datagen()
