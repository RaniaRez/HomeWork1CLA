import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Connection, version

CLIENTQUERY= """CREATE TABLE IF NOT EXISTS clients (
    id integer PRIMARY KEY,
    fname text NOT NULL,
    Lname text NOT NULL,
    Phonenumbr NUMERIC(10) NOT NULL

); """

CARQUERY=  """CREATE TABLE IF NOT EXISTS cars (

    id integer PRIMARY KEY,
    regisnumbr CHAR(7) NOT NULL,
    model VARCHAR(25) NOT NULL,
    Locprice NUMBER NOT NULL,
    client_id Integer,
    FOREIGN KEY (client_id) REFERENCES cleints (id)
) """
def create_connection(db_file):
  
  try:
    conn= sqlite3.connect(db_file)
    print("sql version",sqlite3.version)

  except Error as e:
    print(e)
  return conn

def execute_query(conn,sqlquery) :

  try:
      c=conn.cursor()
      c.execute(sqlquery)

  except Error as e:
      print(e)

  return c

def fetch_rows(conn, query):
    cur=execute_query(conn, query)
    rows= cur.fetchall()
    for row in rows :
     print(row)


SELECTQUERY= "SELECT * FROM clients"      
INSERTQUERY= "INSERT INTO clients (fname,lname,Phonenumbr)   VALUES('Robert', 'Smith', '0000000000')"
UPDATEQUERY="UPDATE clients SET Phonenumbr= 0554635421 WHERE id=1"
DELETEQUERY="DELETE FROM  clients WHERE id=1 "
CONSTRAINTQUERY="SELECT regisnumbr, Locprice, model FROM Cars WHERE Locprice BETWEEN 1491 AND 1886 ORDER BY model LIMIT 10 ;"  

connec=create_connection("new.db")
execute_query(connec,CLIENTQUERY)
execute_query(connec,INSERTQUERY)
fetch_rows(connec, SELECTQUERY)








