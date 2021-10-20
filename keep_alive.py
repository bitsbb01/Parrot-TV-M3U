from flask import Flask
from threading import Thread
from service import ServiceMake

app = Flask('')

@app.route('/')
def home():
  ServiceMake()
  return "Started auto-aupdate!"
  

def  run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()

keep_alive()
