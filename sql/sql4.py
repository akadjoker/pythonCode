import os,sqlite3,sys
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

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

def read_from_db_all():
    c.execute('SELECT * FROM BaseDeDados')
    data = c.fetchall()
    print(data)	
    
def read_from_db():
    c.execute('SELECT * FROM BaseDeDados')
    for row in  c.fetchall():
       print(row)	

def read_from_db_where():
    c.execute("SELECT * FROM BaseDeDados WHERE value=8")
    for row in  c.fetchall():
       print(row)	    

def read_from_db_where_and():
    c.execute("SELECT * FROM BaseDeDados WHERE value<8 AND keyword='Python'")
    for row in  c.fetchall():
       print(row[0])	    
def read_from_db_keyword():
    c.execute("SELECT keyword,unix  FROM BaseDeDados WHERE unix>1")
    for row in  c.fetchall():
       print(row)

def dynamic_data_entry():
    unix= time.time()
    date= str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword='Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO BaseDeDados (unix,datestamep,keyword,value) VALUES (?, ?, ?, ?)",
              (unix,date,keyword,value))
    conn.commit()
	           
def graph_data():
	c.execute('SELECT unix, value FROM BaseDeDados')
	dates=[]
	values=[]
	
	for row in c.fetchall():
	  # print(row[0])
	  # print (datetime.datetime.fromtimestamp(row[0]))
	   dates.append(datetime.datetime.fromtimestamp(row[0]))
	   values.append(row[1])
	   
	plt.plot_date(dates,values,'-')
	plt.show()
	   
	
	               
#read_from_db_all()	
#read_from_db()
#read_from_db_where()
#read_from_db_where_and()
#read_from_db_keyword()

graph_data()
close_db();		
	
