from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_route', methods=['POST'])
def get_route():
    source_address = request.form['source']
    destination_address = request.form['destination']

    # Replace 'your_api_key' with your actual OpenRouteService API key
    api_key = '5b3ce3597851110001cf624815b8e5cae71141a88227df31c3eb9c45'
    geocode_url = "https://api.openrouteservice.org/geocode/search?api_key={}&text={}"
    source_response = requests.get(geocode_url.format(api_key, source_address))
    destination_response = requests.get(geocode_url.format(api_key, destination_address))

    source = "{},{}".format(source_response.json()['features'][0]['geometry']['coordinates'][0], source_response.json()['features'][0]['geometry']['coordinates'][1])
    destination = "{},{}".format(destination_response.json()['features'][0]['geometry']['coordinates'][0], destination_response.json()['features'][0]['geometry']['coordinates'][1])

    directions_url = f"https://api.openrouteservice.org/v2/directions/driving-car?api_key={api_key}&start={source}&end={destination}"
    response = requests.get(directions_url)
    data = response.json()

    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)
