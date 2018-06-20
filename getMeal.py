# 나이스에서 M4ndU님의 파서를 우리학교로 정보를 변경하고 datetime모듈을 동해 급식을 받아, 정리, 저장 #

import requests, re
from bs4 import BeautifulSoup
import datetime
import regex

dt1 = datetime.datetime.today()
todate = dt1.strftime("%Y.%m.%d")

t = ['월','화','수','목','금','토','일',]
r = datetime.datetime.today().weekday()


def get_diet(code, ymd, weekday):
    schMmealScCode = code #int 1조식2중식3석식
    schYmd = ymd #str 요청할 날짜 yyyy.mm.dd
    if weekday == 5 or weekday == 6: #토요일,일요일 버림
        element = " " #공백 반환
    else:
        num = weekday + 1 #int 요청할 날짜의 요일 0월1화2수3목4금5토6일 파싱한 데이터의 배열이 일요일부터 시작되므로 1을 더해줍니다.
        URL = (
                "http://stu.sen.go.kr/sts_sci_md01_001.do?"
                "schulCode=B100000497"
                "&schulCrseScCode=4"
                "&schulKndScCode=04"
                "&schMmealScCode=%d&schYmd=%s" % (schMmealScCode, schYmd)
            )
        #http://stu.AAA.go.kr/ 관할 교육청 주소 확인해주세요.
        #schulCode= 학교고유코드
        #schulCrseScCode= 1유치원2초등학교3중학교4고등학교
        #schulKndScCode= 01유치원02초등학교03중학교04고등학교

        #기존 get_html 함수부분을 옮겨왔습니다.
        html = ""
        resp = requests.get(URL)
        if resp.status_code == 200 : #사이트가 정상적으로 응답할 경우
            html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        element_data = soup.find_all("tr")
        element_data = element_data[2].find_all('td')
        try:
            element = str(element_data[num])

            #filter
            element_filter = ['[', ']', '<td class="textC last">', '<td class="textC">', '</td>', '&amp;', '(h)', '.']
            for element_string in element_filter :
                element = element.replace(element_string, '')
            #줄 바꿈 처리
            element = element.replace('<br/>', '\n')
            #모든 공백 삭제
            element = re.sub(r"\d", "", element)

        #급식이 없을 경우
        except:
            element = "급식이 먹고싶나?\n급식이 없다네 핳핳" # 공백 반환
    return element
   
meal1 = get_diet(2, todate, r) #중식, 2017년 11월 17일, 금요일
meal2 = get_diet(3, todate, r)

mealD = ""
mealM = ""
bar = "=====오늘의 급식=====\n"
error = "주말과 공휴일에는\n아무것도 나타나지 않아욥!"
mealM += todate+ t[r] + "요일\n" + bar + "중식\n"+ meal1+ bar + error
mealD += todate+ t[r] + "요일\n" + bar + "석식\n" + meal2 +bar + error

#print(mealM) #중식출력
#print(mealD) #석식출력
