import mysql.connector
# use lib MySQL-connector-python to work with mysql 8.0+
mydb = mysql.connector.connect(
    host="Localhost",
    user="root",
    passwd="password123",
    # auth_plugin="mysql_native_password",
    database="demodb",
    use_pure= False
  )

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM demodb.` studentinfo`")

myresult = mycursor.fetchall()

print(myresult)

for x in myresult:
    print("id : ", x[0], " name: ", x[1], " marks:", x[2])