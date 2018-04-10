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
	
def close_db():
	c.close()
	conn.close()          
    

def dynamic_data_entry():
    unix= time.time()
    date= str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword='Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO BaseDeDados (unix,datestamep,keyword,value) VALUES (?, ?, ?, ?)",
              (unix,date,keyword,value))
    conn.commit()
	           
    
	
create_table()
for i in range(10):
	dynamic_data_entry()
	time.sleep(1)
close_db()
		
	
