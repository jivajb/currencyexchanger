from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual API key
API_KEY = '0ec769ba4314c19dbd289ec5'
API_URL = f'https://v6.exchangerate-api.com/v6/0ec769ba4314c19dbd289ec5/latest/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exchange', methods=['POST'])
def exchange():
    from_currency = request.form['from_currency'].upper()
    to_currency = request.form['to_currency'].upper()
    amount = float(request.form['amount'])

    response = requests.get(API_URL + from_currency)
    data = response.json()

    if response.status_code != 200 or 'conversion_rates' not in data:
        return jsonify({'error': 'API request failed'})

    exchange_rate = data['conversion_rates'].get(to_currency)
    if exchange_rate is None:
        return jsonify({'error': 'Currency not found'})

    exchanged_amount = amount * exchange_rate

    return jsonify({'exchanged_amount': exchanged_amount, 'exchange_rate': exchange_rate})

if __name__ == '__main__':
    app.run(debug=True)
