from bs4 import BeautifulSoup
from flask import Flask, jsonify, Response, request
from flask_cors import CORS
import requests
import json

from route.data import get_data
from route.weather import get_weather, get_weather_house

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

@app.route('/')
def hello():
    return 'Hello, Flask!'

# 기본적인 GET 요청을 처리하는 라우트
app.add_url_rule('/api/data', 'get_data', get_data, methods=['GET'])
app.add_url_rule('/api/weather', 'get_weather', get_weather, methods=['GET'])
app.add_url_rule('/api/weather-house', 'get_weather_house', get_weather_house, methods=['GET'])

if __name__ == '__main__':
    app.run()

@app.route('/api/item/<item_id>', methods=['GET'])
def get_path_item(item_id):
    output = ""
    path_item = item_id
    output += f"<h1>{path_item}</h1>"
    return output

@app.route('/api/query', methods=['GET'])
def get_query():
    output = ""
    item_type = request.args.get('type', default=None, type=None)
    item_color = request.args.get('color', default=None, type=None)
    output += f"<h1>{item_type}</h1>"
    output += f"<h1>{item_color}</h1>"
    return output

@app.route('/api/register', methods=['POST'])
def post_register():
    data = request.get_json()
    username = data.get('username', None)  # .get 메소드를 사용하여 기본값을 None으로 설정합니다.
    password = data.get('password', None)
    return jsonify({"username": username, "password": password})


# 임의의 데이터, 실제 구현에서는 이 부분에 데이터베이스에서 가져온 데이터나
# 계산된 결과를 넣습니다.

