from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

airports_file = os.path.join(os.path.dirname(__file__), 'airports.json')
with open(airports_file, 'r') as f:
    airports = json.load(f)
airport_dict = {airport['icao'].upper(): airport for airport in airports}
@app.route('/airport/<icao>')
def get_airport(icao):
    icao_upper = icao.upper()
    if icao_upper in airport_dict:
        airport = airport_dict[icao_upper]
        return jsonify({
            "icao": airport['icao'],
            "name": airport['name'],
            "city": airport['city'],
            "country": airport['country']
        })
    else:
        return jsonify({"error": "airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)

