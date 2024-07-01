from flask import Flask, request
import requests







app = Flask(__name__)

API_KEY = '0ec9a8f1fff7464e902105651240107'

@app.route("/")
def welcome():
    return "HNG Stage 1"

    

@app.route("/api/hello")
def index():
    ip_addr = request.remote_addr
    client_name= request.args.get("visitor_name")
    get_location = requests.get(f'http://ip-api.com/json/{ip_addr}')
    location_data = get_location.json()
    city = location_data['city']
    country = location_data['country']
    get_url = requests.get(f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city},{country}')
    weather_data = get_url.json()
    temperature = weather_data['current']['temp_c']
    content = {
        'Client_ip': ip_addr,
        'location': city,
        'greeting': f"Hello {client_name}!, the temperature is {temperature} degrees Celcius in {city}",
        
    }
    return content







if __name__ == '__main__':
    app.run()
