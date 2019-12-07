import os
from bottle import Bottle, request  
import sentry_sdk  
from sentry_sdk.integrations.bottle import BottleIntegration  
  
sentry_sdk.init(
    dsn=os.environ.get("sentry_DNS_сюда"),
    integrations=[BottleIntegration()]
    )  

app = Bottle()
@app.route('/') 
def test():
    return
    
@app.route('/success') 
def success():
    return

@app.route('/fail')  
def index():
    raise RuntimeError("ошибка сервера!")  

app.run(host='localhost', port=8080, debug=True)