from flask import Flask
from threading import Thread
from service import Main

app = Flask('')

@app.route('/')
def home():
  return "401 Unauthorized"
  
@app.route('/update/')
def update():
  Main()
  return "200 OK"

def  run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()

keep_alive()

