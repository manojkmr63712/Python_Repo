#!/usr/bin/python

import psycopg2
import csv
class DataConn:
    def __init__(self):
        try:
	    self.conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='test'")
	    self.conn.autocommit = True
	    self.cursor = self.conn.cursor()
	except:
            print ("cant connect")
    def insert_remi_rec(self):
	try:
	    with open('/home/manoj/Documents/postresql/remitee.tsv',)as fd:
	        rd = csv.reader(fd,delimiter="\t")
                header_data = next(rd)
                da_data = []
                heade_data=1+len(header_data)
                #next(rd,None)
                for row in rd:
		    for i in range(1, heade_data):
		        #print(row[i])
		        da_data.append(row[i])
		    #insert_comm = "INSERT INTO remitees values('"+ row[0] +"','{"+ header_data + "}','{" + da_data + "}')"
	            #print(row[0],header_data,da_data)
		    #print(insert_comm)
		    head_data = ', '.join('"{0}"'.format(w) for w in header_data)
	            da1_data = ', '.join('"{0}"'.format(w) for w in da_data)
		    self.cursor.execute("INSERT INTO remitees values('"+ row[0] +"','{"+ head_data + "}','{" + da1_data + "}')")
	            del da_data[:]
	    print("Data Successfully inserted into remitess table")
	except:
	    print("There is an error in data pipeline")
    def insert_migr_rec(self):
        try:
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
                    #insert_comm = "INSERT INTO remitees values('"+ row[0] +"','{"+ header_data + "}','{" + da_data + "}')"
                    #print(row[0],header_data,da_data)
                    #print(insert_comm)
                    head_data = ', '.join('"{0}"'.format(w) for w in header_data)
                    da1_data = ', '.join('"{0}"'.format(w) for w in da_data)
                    self.cursor.execute("INSERT INTO migration values('"+ row[0] +"','{"+ head_data + "}','{" + da1_data + "}')")
                    del da_data[:]
            print("Data Successfully inserted into migration table")
        except IndexError:
            print("Data Insered success fully but. There is an Index error")

if __name__ == '__main__':
    dabaconn = DataConn()
    dabaconn.insert_remi_rec()
    dabaconn.insert_migr_rec()
