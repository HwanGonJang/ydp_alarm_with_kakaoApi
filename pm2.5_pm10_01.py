from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

url_base = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='
url_syb1 = '%EB%8F%99%EC%9E%91%EA%B5%AC+%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80'
url_syb2 = '%EB%8F%99%EC%9E%91%EA%B5%AC+%EC%B4%88%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80'

PM10url = url_base + url_syb1
PM25url = url_base + url_syb2
hdr1 = {'referer': url_base + url_syb1, 'User-Agent':'Mozilla/5.0', 'referer' : 'http://www.naver.com'}
hdr2 = {'referer': url_base + url_syb2, 'User-Agent':'Mozilla/5.0', 'referer' : 'http://www.naver.com'}

req1 = Request(PM10url, headers=hdr1)
page1 = urlopen(req1)
req2 = Request(PM25url, headers=hdr2)
page2 = urlopen(req2)

soup1 = BeautifulSoup(page1,'html.parser')
soup2 = BeautifulSoup(page2,'html.parser')

pm10 = soup1.find('em','main_figure').get_text()
pm25 = soup2.find('em','main_figure').get_text()

if(int(pm25)<=15):
    warning1 = '\n상태 : 좋음\n\n일반인 : 굳'
elif(16<=int(pm25) and int(pm25)<=35):
    warning1 = '\n상태 : 보통\n\n민감군 : 실외활동 시 특별히 행동에 제약은 없으나 몸 상태에 따라 유의하여 활동'
elif(36<=int(pm25) and int(pm25)<=75):
   warning1 = '\n상태 : 나쁨\n\n일반인 : 장시간 또는 무리한 실외활동 제한, 특히 눈이 아프거나, 기침, 목의 통증으로 불편한 사람은 실외활동을 피해야 함\n\n민감군 : 장시간 또는 무리한 실외활동 제한, 특히 천식환자는 실외활동 시 흡입기를 더 자주 사용할 필요가 있음'
elif(76<=int(pm25)):
    warning1 = '\n상태 : 매우나쁨\n\n일반인 : 장시간 또는 무리한 실외 활동제한, 기침이나 목의 통증 등이 있는 사람은 실외활동을 피해야 함\n\n민감군 : 가급적 실내 활동만 하고 실외 활동시 의사와 상의'

if(int(pm25)<=30):
    warning2 = '\n상태 : 좋음\n\n일반인 : 굳'
elif(31<=int(pm25) and int(pm25)<=80):
    warning2 = '\n상태 : 보통\n\n민감군 : 실외활동 시 특별히 행동에 제약은 없으나 몸 상태에 따라 유의하여 활동'
elif(81<=int(pm25) and int(pm25)<=150):
   warning2 = '\n상태 : 나쁨\n\n일반인 : 장시간 또는 무리한 실외활동 제한, 특히 눈이 아프거나, 기침, 목의 통증으로 불편한 사람은 실외활동을 피해야 함\n\n민감군 : 장시간 또는 무리한 실외활동 제한, 특히 천식환자는 실외활동 시 흡입기를 더 자주 사용할 필요가 있음'
elif(151<=int(pm25)):
    warning2 = '\n상태 : 매우나쁨\n\n일반인 : 장시간 또는 무리한 실외 활동제한, 기침이나 목의 통증 등이 있는 사람은 실외활동을 피해야 함\n\n민감군 : 가급적 실내 활동만 하고 실외 활동시 의사와 상의'

resultpm25 = '동작구 초미세먼지: ' + pm25 + warning1 + '\n\nhttps://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%8F%99%EC%9E%91%EA%B5%AC+%EC%B4%88%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80 에서 수집된 정보이고, 사이트별로 오차가 있을수 있습니다.'
resultpm10 = '동작구 미세먼지: ' + pm10 + warning2 + '\n\nhttps://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%8F%99%EC%9E%91%EA%B5%AC+%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80 에서 수집된 정보이고, 사이트별로 오차가 있을수 있습니다.'
#========================================미세먼지, 초미세먼지end
