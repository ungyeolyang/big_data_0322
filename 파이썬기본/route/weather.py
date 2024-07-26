import requests
from bs4 import BeautifulSoup
import json
import datetime

def get_weather():
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

    # HTTP GET 요청
    response = requests.get(url)
    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    output = ""

    for loc in soup.select("location"):
        output += f"<h3>{loc.select_one('city').string}<h3>"
        output += f"날씨 : {loc.select_one('wf').string}</br>"
        output += f"최저/최고 기온 : {loc.select_one('tmn')}/{loc.select_one('tmx')}</hr>"

    return output

def get_weather_house():
    nx_val = request.args.get('x',default=None, type=None)

    API_KEY = '8Y6SP1oo%2FPy4%2F0DknsKGwe1oHUWtaitlRaHZxZ6Zay0bxN%2FMm0sjB%2BoAWHyk5S6wLyH2%2B9L4DamqYzmH%2F7Asqw%3D%3D'
    API_KEY_decode = requests.utils.unquote(API_KEY)

    now = datetime.datetime.now()
    date = now.strftime('%Y%m%d')

    time = now.strftime('%H%M')

    if now.minute < 30:
        now = now - datetime.timedelta(minutes=30)
        time = now.strftime('%H%M')
    else:
        time = now.strftime('%H%M')

    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

    baseDate = date
    baseTime = time


    nx_val = 62
    ny_val = 126

    num_of_rows = 6

    page_no = 1

    data_type = 'JSON'

    req_parameter = {'serviceKey': API_KEY_decode,
                     'nx': nx_val, 'ny': ny_val,
                     'base_date': baseDate, 'base_time': baseTime,
                     'pageNo': page_no, 'numOfRows': num_of_rows,
                      'dataType': data_type}


    try:
        response = requests.get(url, params=req_parameter)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making a request: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)


    dict_data = response.json()


    print(json.dumps(dict_data, indent=2))


    weather_items = dict_data['response']['body']['items']['item']

    print(f"[ 발표 날짜 : {weather_items[0]['baseDate']} ]")
    print(f"[ 발표 시간 : {weather_items[0]['baseTime']} ]")

    weather_data = {}

    for k in range(len(weather_items)):
        weather_item = weather_items[k]
        obsrValue = weather_item['obsrValue']
        if weather_item['category'] == 'T1H':
            weather_data['tmp'] = f"{obsrValue}℃"
        elif weather_item['category'] == 'REH':
            weather_data['hum'] = f"{obsrValue}%"
        elif weather_item['category'] == 'RN1':
            weather_data['pre'] = f"{obsrValue}mm"
    # 딕셔너리를 JSON 형태로 변환
    json_weather = json.dumps(weather_data, ensure_ascii=False, indent=4)
    return json_weather
