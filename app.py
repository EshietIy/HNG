from flask import Flask
from flask import request
import requests


app = Flask(__name__)
@app.route('/api/hello')
def hello():

    name = str(request.args.get('visitor_name'))
    ip = requests.get('https://api.ipify.org?format=json').json()
    location = requests.get(f'https://ipapi.co/{ip["ip"]}/json/').json()
    city = location.get("city")

    message = f"Hello, {name}, the temperature is 10 degrees Celcius in {city}"
    if name == None:
        return {
            "Name": "Not given"
            }
    else:
        return {
            "client_ip": ip.get("ip"),
            "location": location.get("city"),
            "greeting": message 
        }

if __name__ == '__main__':
    app.run(debug=True)