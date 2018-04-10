import os,sqlite3,sys
import time
import datetime
import random

conn=sqlite3.connect('data.db')
c=conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS BaseDeDados(unix REAL,datestamep TEXT,keyword TEXT,value REAL)')
	
def data_entry():
	c.execute("INSERT INTO BaseDeDados values(145,'2018-01-01','djoker',1)")
	conn.commit()
	c.close()
	conn.close()
	

    
	
create_table()
data_entry()	

		
	
