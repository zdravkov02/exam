import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  with open('app.tpl') as f:
    template = f.read()

  facts = ""

  db_host = os.getenv('DB_HOST', 'con-storage')
  db_user = os.getenv('DB_USER', 'root')
  db_pass = os.getenv('DB_PASS', 'ExamPa$$w0rd')
  db_name = os.getenv('DB_NAME', 'animal_facts')

  try:
    mydb = mysql.connector.connect(
      host = db_host,
      user = db_user,
      password = db_pass,
      database = db_name
    )
    cursor = mydb.cursor()
  
    cursor.execute("SELECT CONCAT('<li>', fact, '</li>') html_fact FROM facts ORDER BY id DESC LIMIT 10")
  
    records = cursor.fetchall()
 
    if cursor.rowcount == 0:
      facts = 'No data found yet.'

    for row in records:
      facts = facts + row[0]
  
    cursor.close()
  except:
    facts = "Error: Something happened while trying to talk to the database."

  result = template.replace("{FACTS}", facts)

  with open('app.dat') as f:
    build = f.read()

  result = result.replace("{BUILD}", build)

  return result
