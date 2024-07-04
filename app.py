from flask import Flask
from flask import request
import requests


app = Flask(__name__)
@app.route('/api/hello')
def hello():

    name = str(request.args.get('visitor_name'))
    test_IP = request.environ.get('HTTP_X_FORWARDED_FOR')
    print(f"test IP {test_IP}")
    temp_ip = request.environ.get('HTTP_X_FORWARDED_FOR')
    if temp_ip is None:
        ip = request.remote_addr
    else:
        ip = temp_ip
    location = requests.get(f'https://ipapi.co/{ip}/json/').json()
    city = location.get("city")

    message = f"Hello, {name}, the temperature is 10 degrees Celcius in {city}"
    if name == None:
        return {
            "Name": "Not given"
            }
    else:
        return {
            "client_ip": ip,
            "location": location.get("city"),
            "greeting": message 
        }

if __name__ == '__main__':
    app.run(debug=True)