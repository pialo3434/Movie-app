import mysql.connector
from mysql.connector import Error

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="TPSIPL1022_SQL"
)
