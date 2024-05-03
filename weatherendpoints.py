from flask import Flask, jsonify, request  # This is using statement in C#

app = Flask(__name__)  # Here we define a flask app which we will run at the end

forecasts = [
    {"Id": 1, "Date": "2024-04-22", "TemperatureC": 25, "Summary": "Sunny"},
    {"Id": 2, "Date": "2024-04-23", "TemperatureC": 18, "Summary": "Cloudy"}
] # this is how we define list in python

@app.route('/weatherforecast', methods=['GET'])  # routing similar to attribute routing in .net
def get_forecasts(): # in python we define methods by using def
    return jsonify(forecasts)

@app.route('/weatherforecast/<int:id>', methods=['GET'])
def get_forecast(id):
    forecast = next((f for f in forecasts if f["Id"] == id), None)
    if forecast:
        return jsonify(forecast)
    else:
        return jsonify({"error": "Forecast not found"}), 404

@app.route('/weatherforecast', methods=['POST'])
def create_forecast():
    data = request.get_json()
    data["Id"] = len(forecasts) + 1
    forecasts.append(data)
    return jsonify(data), 201

@app.route('/weatherforecast/<int:id>', methods=['PUT'])
def update_forecast(id):
    forecast = next((f for f in forecasts if f["Id"] == id), None)
    if forecast:
        data = request.get_json()
        forecast.update(data)
        return jsonify(forecast)
    else:
        return jsonify({"error": "Forecast not found"}), 404

@app.route('/weatherforecast/<int:id>', methods=['DELETE'])
def delete_forecast(id):
    forecast = next((f for f in forecasts if f["Id"] == id), None)
    if forecast:
        forecasts.remove(forecast)
        return '', 204
    else:
        return jsonify({"error": "Forecast not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)  #This starts the flask app which we defined in the beginning in debug mode
# __name__ is a built-in variable and represents the name of the current module.
# When we run python file, Python sets the __name__ variable  '__main__'.