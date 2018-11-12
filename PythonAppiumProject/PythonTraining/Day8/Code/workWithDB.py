import mysql.connector

#create database handle
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password123",
  auth_plugin='mysql_native_password',
  database='demodb'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM studentinfo")  # this statement will execute the query at the db level
#and fetch the result. 

myresult = mycursor.fetchall()
print (myresult)# a list of tuples

#printing row wise information by iterating the list
for x in myresult:
    print("id:",x[0], " name:", x[1], " marks:", x[2])
 
   