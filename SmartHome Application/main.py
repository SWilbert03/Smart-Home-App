import mysql.connector
from GUI_Project.login import *

db=mysql.connector.connect(host="localhost", user="202000679", password="iee", database="smarthome_database")

cursor=db.cursor()
select = "SELECT * FROM USERS"
cursor.execute(select)

for values in cursor:
    print(values)

