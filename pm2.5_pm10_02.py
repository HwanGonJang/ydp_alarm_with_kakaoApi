# 같은 폴더의 pm2.5_pm10.py는 네이버의 페이지가 변경되어 http://aqicn.org/city/korea/seoul/dongjak-gu/kr/ 사이트로 변경됨

from bs4 import BeautifulSoup
from urllib.request import urlopen


url_base = 'http://aqicn.org/city/korea/seoul/'
url_syb = 'dongjak-gu/kr/'

page = urlopen(url_base + url_syb)
soup = BeautifulSoup(page, 'html.parser')

aqiwgtvalue = soup.find(id= 'aqiwgtvalue').get_text()

if(int(aqiwgtvalue)<=50):
    warning = '\n상태 : 좋음\n\n대기오염 관련 질환자군에서도 영향이 유발되지 않을 수준'
elif(51<=int(aqiwgtvalue) and int(aqiwgtvalue)<=100):
    warning = '\n상태 : 보통\n\n환자군에게 만성 노출시 경미한 영향이 유발될 수 있는 수준'
elif(101<=int(aqiwgtvalue) and int(aqiwgtvalue)<=150):
   warning = '\n상태 : 민감군영향\n\n환자군 및 민감군에게 유해한 영향이 유발될 수 있는 수준'
elif(151<=int(aqiwgtvalue) and int(aqiwgtvalue)<=200):
    warning = '\n상태 : 나쁨\n\n환자군 및 민감군(어린이, 노약자 등)에게 유해한 영향 유발, 일반인도 건강상 불쾌감을 경험할 수 있는 수준'
elif(201<=int(aqiwgtvalue) and int(aqiwgtvalue)<=300):
    warning = '\n상태 : 매우나쁨\n\n환자군 및 민감군에게 급성 노출시 심각한 영향 유발, 일반인도 약한 영향이 유발될 수 있는 수준'
elif(301<=int(aqiwgtvalue)):
    warning = '\n상태 : 위험\n\n환자군 및 민감군에게 응급 조치가 발생되거나, 일반인에게 유해한 영향이 유발될 수 있는 수준'


aqi = "동작구 서울 대기질 지수 : " + aqiwgtvalue + "\n" + warning + "\n\n위 정보는 http://aqicn.org/city/korea/seoul/dongjak-gu/kr/에서 받아온 AQI(대기 질 지수)정보 입니다."

#print(aqi)
