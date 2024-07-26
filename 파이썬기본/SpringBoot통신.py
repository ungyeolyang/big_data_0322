import requests
import json

data = {
    "id" : "곰돌이사육사233",
    "pwd" : "sphb8250"
}

url = "http://localhost:8111/auth/python"
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

# 서버 응답 확인
if response.status_code == 200:
    if response.headers.get('Content-Type') == 'application/json':
        data = response.json()
    print(data)
    print("데이터가 성공적으로 전송되었습니다.")
else:
    print("데이터 전송에 실패했습니다. 응답 코드:", response.status_code)