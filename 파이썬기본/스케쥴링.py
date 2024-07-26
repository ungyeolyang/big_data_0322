import schedule
import time
import requests # 서버와 http 동기 통신을 하기 위해서 사용
from bs4 import BeautifulSoup

def perform_web_crawling():
    url ="http://naver.com"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
    print(soup)

def job():
    print("웹 크롤링을 수행 합니다.")
    perform_web_crawling()

# schedule.every().day.at("09:45").do(job)
# schedule.every(1).minutes.at("09:45").do(job)

while True:
    schedule.run_pending() #대기 중인 작업을 수행
    time.sleep(1) # 1초대기
