import mysql.connector
import config

def database_connection():
   connection = mysql.connector.connect(
      user=config.USER,
      password=config.PASSWORD,
      host=config.HOST,
      database=config.DATABASE
)
   return connection

