from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests, re
from bs4 import BeautifulSoup
import datetime
import urllib.request
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
    
#meal = get_diet(2, "2018.06.15", 4) #중식, 2017년 11월 17일, 금요일
meal1 = get_diet(2, todate, r) #중식, 2017년 11월 17일, 금요일
meal2 = get_diet(3, todate, r)

mealD = ""
mealM = ""
bar = "=====오늘의 급식=====\n"
error = "주말과 공휴일에는\n아무것도 나타나지 않아욥!"
mealM += todate+ t[r] + "요일\n" + bar + "중식\n"+ meal1+ bar + error
mealD += todate+ t[r] + "요일\n" + bar + "석식\n" + meal2 +bar + error
#========================================오늘의급식end
#========================================오늘의 명언

#========================================오늘의 명언end
sub = t[r] + "요일 시간표\n"
bar = "==========\n"
danger = "시간표가변경될수있습니다.\n오타제보"
#========================================class기틀end
#========================================class11
if t[r] == "월":
    classTime = "1교시: 한A\n2교시: 국B\n3교시: 수학\n4교시: 통사\n5교시: 영A\n6교시: 과B\n7교시: 체육\n"
    class11 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 과C\n2교시: 체육\n3교시: 영B\n4교시: 진로\n5교시: 국A\n6교시: 수학\n7교시: 한A\n"
    class11 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 미술\n2교시: 미술\n3교시: 영A\n4교시: 통사\n5교시: 수학\n6교시: 과A\n"
    class11 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 국B\n2교시: 수학\n3교시: 실험\n4교시: 영B\n5교시: 통사\n6교시: 기술\n7교시: 기술\n"
    class11 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 과A\n2교시: 한A\n3교시: 미술\n4교시: 국A\n5교시: 창체\n6교시: 창체\n"
    class11 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class11 = sub + bar + classTime + bar + danger
#========================================class11end
#========================================class12
if t[r] == "월":
    classTime = "1교시: 과A\n2교시: 통사\n3교시: 수학\n4교시: 국A\n5교시: 영A\n6교시: 미술\n7교시: 미술\n"
    class12 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 체육\n2교시: 국B\n3교시: 영B\n4교시: 통사\n5교시: 실험\n6교시: 수학\n7교시: 과C\n"
    class12 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 통사\n2교시: 한B\n3교시: 영A\n4교시: 과B\n5교시: 수학\n6교시: 국B\n"
    class12 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 미술\n2 교시: 수학\n3교시: 한A\n4교시: 영B\n5교시: 국A\n6교시: 과A\n7교시: 진로\n"
    class12 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 체육\n2 교시: 기술\n3교시: 기술\n4교시: 한A\n5교시: 창체\n6교시: 창체\n"
    class12 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class12 = sub + bar + classTime + bar + danger
#======================================class12end
#======================================class13
if t[r] == "월":
    classTime = "1교시: 영A\n2교시: 체육\n3교시: 한B\n4교시: 미술\n5교시: 과A\n6교시: 수학\n7교시: 국B\n"
    class13 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 통사\n2교시: 과A\n3교시: 국A\n4교시: 영B\n5교시: 한A\n6교시: 기술\n7교시: 기술\n"
    class13 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 과B\n2교시: 통사\n3교시: 한A\n4교시: 체육\n5교시: 국A\n6교시: 수힉\n"
    class13 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 영A\n2교시: 통사\n3교시: 과C\n4교시: 수학\n5교시: 진로\n6교시: 미술\n7교시: 미술\n"
    class13 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 영B\n2교시: 실험\n3교시:수학\n4교시:국B\n5교시: 창체\n6교시: 창체\n"
    class13 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class13 = sub + bar + classTime + bar + danger
#======================================class13end
#======================================class14
if t[r] == "월":
    classTime = "1교시: 영A\n2교시: 통사\n3교시: 진로\n4교시: 한A\n5교시: 국B\n6교시: 수학\n7교시: 과B\n"
    class14 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 국B\n2교시: 기술\n3교시: 기술\n4교시: 영B\n5교시: 미술\n6교시: 미술\n7교시: 통사\n"
    class14 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 한B\n2교시: 국A\n3교시: 체육\n4교시: 통사\n5교시: 과C\n6교시: 수학\n"
    class14 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 영A\n2교시: 실험\n3교시: 과A\n4교시: 수학\n5교시: 한A\n6교시: 체육\n7교시: 국A\n"
    class14 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 영B\n2교시: 과A\n3교시:수학\n4교시:미술\n5교시: 창체\n6교시: 창체\n"
    class14 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class14 = sub + bar + classTime + bar + danger
#======================================class14end
#======================================class15
if t[r] == "월":
    classTime = "1교시: 수학\n2교시: 진로\n3교시: 국B\n4교시: 과A\n5교시: 기술\n6교시: 기술\n7교시: 음악\n"
    class15 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 음악\n2교시: 통사\n3교시: 수학\n4교시: 과B\n5교시: 국B\n6교시: 영A\n7교시: 체육\n"
    class15 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 통사\n2교시: 수학\n3교시: 과A\n4교시: 한A\n5교시: 영B\n6교시: 국A\n"
    class15 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 한A\n2교시: 영A\n3교시: 국A\n4교시: 과A\n5교시: 실험\n6교시: 음악\n7교시:수학\n"
    class15 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 영B\n2교시: 체육\n3교시: 영B\n4교시: 통사\n5교시: 창체\n6교시: 창체\n"
    class15 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class15 = sub + bar + classTime + bar + danger
#======================================class15end
#======================================class16
if t[r] == "월":
    classTime = "1교시: 수학\n2교시: 한A\n3교시: 과C\n4교시: 실험\n5교시: 통사\n6교시: 체육\n7교시: 국A\n"
    class16 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 국A\n2교시: 한A\n3교시: 수학\n4교시: 통사\n5교시: 과A\n6교시: 영A\n7교시: 음악\n"
    class16 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 과A\n2교시: 수학\n3교시: 기술\n4교시: 기술\n5교시: 영B\n6교시: 과B\n"
    class16 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 음악\n2교시: 영A\n3교시: 통사\n4교시: 체육\n5교시: 국B\n6교시: 한B\n7교시:수학\n"
    class16 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 국B\n2교시: 진로\n3교시: 영B\n4교시:음악\n5교시: 창체\n6교시: 창체\n"
    class16 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class16 = sub + bar + classTime + bar + danger
#======================================class16end
#======================================class17
if t[r] == "월":
    classTime = "1교시: 국A\n2교시: 음악\n3교시: 영A\n4교시: 체육\n5교시: 수학\n6교시: 통사\n7교시: 한A\n"
    class17 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 영B\n2교시: 수학\n3교시: 한A\n4교시: 실험\n5교시: 음악\n6교시: 과A\n7교시: 국B\n"
    class17 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 체육\n2교시: 국B\n3교시: 음악\n4교시: 한B\n5교시: 진로\n6교시: 영B\n"
    class17 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 수학\n2교시: 국A\n3교시: 기술\n4교시: 기술\n5교시: 통사\n6교시: 영A\n7교시:과A\n"
    class17 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 국A\n2교시: 통사\n3교시: 실험\n4교시:수\n5교시: 창체\n6교시: 창체\n"
    class17 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class17 = sub + bar + classTime + bar + danger
#======================================class17end
#======================================class18
if t[r] == "월":
    classTime = "1교시: 기술\n2교시: 기술\n3교시: 영A\n4교시: 음악\n5교시: 수학\n6교시: 국A\n7교시: 과A\n"
    class18 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 영B\n2교시: 수학\n3교시: 과A\n4교시: 통사\n5교시: 진로\n6교시: 체육\n7교시: 한A\n"
    class18 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 한A\n2교시: 음악\n3교시: 과C\n4교시: 국B\n5교시: 통사\n6교시: 국B\n"
    class18 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 수학\n2교시: 국B\n3교시: 한B\n4교시: 과B\n5교시: 음악\n6교시: 영A\n7교시:체육\n"
    class18 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 국A\n2교시: 통사\n3교시: 실험\n4교시:수학\n5교시: 창체\n6교시: 창체\n"
    class18 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class18 = sub + bar + classTime + bar + danger
#======================================class18end
#======================================class21
if t[r] == "월":
    classTime = "1교시: 미적\n2교시: 일어\n3교시: 윤사\n4교시: 문C\n5교시: 진로\n6교시: 영B\n7교시: 세계\n"
    class21 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 세계\n2교시: 문A\n3교시: 생명\n4교시: 영A\n5교시: 윤사\n6교시: 세지\n7교시: 체육\n"
    class21 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 체육\n2교시: 세지\n3교시: 문B\n4교시: 영A\n5교시: 미술\n6교시: 미적\n"
    class21 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 문A\n2교시: 윤사\n3교시: 환경\n4교시: 미술\n5교시: 미적\n6교시: 일어\n7교시: 세지\n"
    class21 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 일어\n2교시: 미적\n3교시: 영A\n4교시: 문B\n5교시: 창체\n6교시: 창체\n"
    class21 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class21 = sub + bar + classTime + bar + danger
#======================================class21end
#======================================class22
if t[r] == "월":
    classTime = "1교시: 일어\n2교시: 영A\n3교시: 세지\n4교시: 세계\n5교시: 미적\n6교시: 문B\n7교시: 진로\n"
    class22 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 세지\n2교시: 세계\n3교시: 영B\n4교시: 미적\n5교시: 문A\n6교시: 생명\n7교시: 일어\n"
    class22 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 미술\n2교시: 영A\n3교시: 미적\n4교시: 윤사\n5교시: 문C\n6교시: 세지\n"
    class22 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 미술\n2교시: 환경\n3교시: 미적\n4교시: 문B\n5교시: 영A\n6교시: 체육\n7교시: 윤사\n"
    class22 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 체육\n2교시: 문A\n3교시: 일어\n4교시: 윤사\n5교시: 창체\n6교시: 창체\n"
    class22 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class22 = sub + bar + classTime + bar + danger
#=======================================class22end
#======================================class23
if t[r] == "월":
    classTime = "1교시: 세계\n2교시: 윤사\n3교시: 문A\n4교시: 환경\n5교시: 미적\n6교시: 영A\n7교시: 세지\n"
    class23 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 문B\n2교시: 윤사\n3교시: 일중\n4교시: 미적\n5교시: 영B\n6교시: 세계\n7교시: 미술\n"
    class23 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 영A\n2교시: 미적\n3교시: 일중\n4교시: 생명\n5교시: 체육\n6교시: 문C\n"
    class23 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 미적\n2교시: 영A\n3교시: 체육\n4교시: 세지\n5교시: 일중\n6교시: 문B\n7교시: 문A\n"
    class23 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 윤사\n2교시: 미술\n3교시: 세지\n4교시: 진로\n5교시: 창체\n6교시: 창체\n"
    class23 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class23 = sub + bar + classTime + bar + danger
#======================================class23end
#======================================class24
if t[r] == "월":
    classTime = "1교시: 문B\n2교시: 미적\n3교시: 영B\n4교시: 세지\n5교시: 진로\n6교시: 환경\n7교시: 체육\n"
    class24 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 영A\n2교시: 세지\n3교시: 일중\n4교시: 문B\n5교시: 미술\n6교시: 윤사\n7교시: 미적\n"
    class24 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 영A\n2교시: 윤사\n3교시: 일중\n4교시: 미적\n5교시: 문A\n6교시: 생명\n"
    class24 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 윤사\n2교시: 세지\n3교시: 문A\n4교시: 세계\n5교시: 일중\n6교시: 미적\n7교시: 영A\n"
    class24 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 미술\n2교시: 세계\n3교시: 체육\n4교시: 문C\n5교시: 창체\n6교시: 창체\n"
    class24 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class24 = sub + bar + classTime + bar + danger
#=======================================class24end
#========================================class26
if t[r] == "월":
    classTime = "1교시: 물리\n2교시: 생물\n3교시: 미적\n4교시: 미술\n5교시: 영A\n6교시: 문A\n7교시: 문C\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 미적\n2교시: 영A\n3교시: 문B\n4교시: 일본어/중국어\n5교시: 체육\n6교시: 진로\n7교시: 화학\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 지학\n2교시: 문A\n3교시: 물리\n4교시: 미술\n5교시: 일본어/중국어\n6교시: 미적A\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 체육\n2교시: 일본어/중국어\n3교시: 미적\n4교시: 영B\n5교시: 미적\n6교시: 지학\n7교시: 문B\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 미적\n2교시: 화학\n3교시: 생물\n4교시: 영A\n5교시: 창체\n6교시: 창체\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class26 = sub + bar + classTime + bar + danger
#=================================class26end
#=================================class25
if t[r] == "월":
    classTime = "1교시: 영B\n2교시: 미적\n3교시: 체육\n4교시: 물리\n5교시: 문A\n6교시: 지학\n7교시: 진로\n"
    class25 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 영A\n2교시: 체육\n3교시: 문A\n4교시: 일본어/중국어\n5교시: 화학A\n6교시: 미적\n7교시: 미적\n"
    class25 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 생물\n2교시: 문B\n3교시: 지학\n4교시: 미적\n5교시: 일본어/중국어\n6교시: 미술\n"
    class25 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 영A\n2교시: 일본어/중국어\n3교시: 미술\n4교시: 화학\n5교시: 생물\n6교시: 문C\n7교시: 미적\n"
    class25 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 물리\n2교시: 영A\n3교시: 문B\n4교시: 미적\n5교시: 창체\n6교시: 창체\n"
    class25 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class25 = sub + bar + classTime + bar + danger
#===============================class25end
#===============================class27
if t[r] == "월":
    classTime = "1교시: 생물\n2교시: 미적\n3교시: 화학\n4교시: 영A\n5교시: 체육\n6교시: 미적\n7교시: 미술\n"
    class27 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 융합\n2교시: 미적\n3교시: 지학\n4교시: 문C\n5교시: 생물\n6교시: 문B\n7교시: 영A\n"
    class27 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 문A\n2교시: 물리\n3교시: 화학\n4교시: 미적\n5교시: 문B\n6교시: 체육\n"
    class27 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 미적\n2교시: 실험\n3교시: 실험\n4교시: 문A\n5교시: 영B\n6교시: 미술\n7교시: 영A\n"
    class27 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 지학\n2교시: 진로\n3교시: 미적\n4교시: 물리\n5교시: 창체\n6교시: 창체\n"
    class27 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class27 = sub + bar + classTime + bar + danger
#===============================class27end
#=============================class28
if t[r] == "월":
    classTime = "1교시:  체육\n2교시:  물리\n3교시:  영A\n4교시:  미적\n5교시:  문B\n6교시:  화학\n7교시:  생물\n"
    class28 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시:  문C\n2교시:  미술\n3교시: 체육\n4교시:  영A\n5교시:  미적\n6교시:  융합\n7교시:  지학\n"
    class28 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시:  미적\n2교시:  미술\n3교시:  미적\n4교시:  지학\n5교시:  영A\n6교시:  문A\n"
    class28 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시:  영B\n2교시:  문B\n3교시:  화학\n4교시:  미적\n5교시:  실험\n6교시:  실험\n7교시:  진로\n"
    class28 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시:  생물\n2교시:  미적\n3교시:  물리\n4교시:  문A\n5교시:  창체\n6교시:  창체\n"
    class28 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class28 = sub + bar + classTime + bar + danger
#==============================class28end
#===============================class31
if t[r] == "월":
    classTime = "1교시: 작A\n2교시: 한A\n3교시: 한지\n4교시: 지학\n5교시: 영A\n6교시: 체육\n7교시: 확통\n"
    class31 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 영A\n2교시: 사문\n3교시: 확통\n4교시: 작B\n5교시: 한지\n6교시: 생윤\n7교시: 한B\n"
    class31 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 진로\n2교시: 체육\n3교시: 작C\n4교시: 생윤\n5교시: 사문\n6교시: 영B\n"
    class31 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 사문A\n2교시: 한B\n3교시: 한문\n4교시: 한지\n5교시: 확통\n6교시: 영A\n7교시: 작A\n"
    class31 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 한A\n2교시: 작B\n3교시: 영B\n4교시: 생윤\n5교시: 창체\n6교시: 창체\n"
    class31 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class31 = sub + bar + classTime + bar + danger
#===============================class31end
#===============================class32
if t[r] == "월":
    classTime = "1교시: 작B\n2교시: 확통\n3교시: 사문\n4교시: 생윤\n5교시: 진로\n6교시: 영A\n7교시: 지학\n"
    class32 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 생윤\n2교시: 작A\n3교시: 한B\n4교시: 영B\n5교시: 체육\n6교시: 한지\n7교시: 사문\n"
    class32 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 한A\n2교시: 한지\n3교시: 영A\n4교시: 작A\n5교시: 한문\n6교시: 확통\n"
    class32= sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 작CA\n2교시: 체육\n3교시: 한A\n4교시: 확통\n5교시: 생윤\n6교시: 영B\n7교시: 한지\n"
    class32 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 한B\n2교시: 사문\n3교시: 작B\n4교시: 영A\n5교시: 창체\n6교시: 창체\n"
    class32 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class32 = sub + bar + classTime + bar + danger
#===============================class32end
#===============================class33
if t[r] == "월":
    classTime = "1교시: 한지\n2교시: 생윤\n3교시: 작B\n4교시: 사문\n5교시: 체육\n6교시: 확통\n7교시: 영B\n"
    class33 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 확통\n2교시: 영A\n3교시: 진로\n4교시: 사문\n5교시: 생윤\n6교시: 작C\n7교시: 한A\n"
    class33 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 생윤\n2교시: 한C\n3교시: 체육\n4교시: 한지\n5교시: 영A\n6교시: 작A\n"
    class33 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 한A\n2교시: 사문\n3교시: 영A\n4교시: 작B\n5교시: 지학\n6교시: 확통\n7교시: 영B\n"
    class33 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 작A\n2교시: 한지\n3교시: 한문\n4교시: 한B\n5교시: 창체\n6교시: 창체\n"
    class33 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class33 = sub + bar + classTime + bar + danger
#===============================class33end
#===============================class34
if t[r] == "월":
    classTime = "1교시: 작C\n2교시: 영B\n3교시: 체육\n4교시: 확통\n5교시: 한지\n6교시: 사문\n7교시: 생윤\n"
    class34 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 한B\n2교시: 한A\n3교시: 한지\n4교시: 지학\n5교시: 영A\n6교시: 작B\n7교시: 한문\n"
    class34 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 사문\n2교시: 한A\n3교시: 작A\n4교시: 영A\n5교시: 생윤\n6교시: 체육\n"
    class34 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 진로\n2교시: 작비\n3교시: 확통\n4교시: 영A\n5교시: 확통\n6교시: 생윤\n7교시: 한B\n"
    class34 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 한지\n2교시: 영A\n3교시: 확통\n4교시: 작A\n5교시: 창체\n6교시: 창체\n"
    class34 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class34 = sub + bar + classTime + bar + danger
#===============================class34end
#===============================class35
if t[r] == "월":
    classTime = "1교시: 생윤\n2교시: 한문\n3교시: 한문\n4교시: 중국어\n5교시: 진로\n6교시: 진로"
    class35 = sub + bar + classTime + bar + danger

elif t[r] == "토" or "일" or "화" or "수" or "목" or "금":
    classTime = "월요일을 제외한 날은 수업이 없습니다\n"
    class35 = sub + bar + classTime + bar + danger
#===============================class35end
#===============================class36
if t[r] == "월":
    classTime = "1교시: 확통\n2교시: 영A\n3교시: 물리\n4교시: 한A\n5교시: 작B\n6교시: 지학\n7교시: 기벡\n"
    class36 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 법정\n2교시: 물리\n3교시: 기벡\n4교시: 진로\n5교시: 작A\n6교시: 체육\n7교시: 영A\n"
    class36 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 지학\n2교시: 확통\n3교시: 영B\n4교시: 작B\n5교시: 기벡\n6교시: 한B\n"
    class36 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 영A\n2교시: 기벡\n3교시: 법정\n4교시: 한B\n5교시: 체육\n6교시: 작A\n7교시: 물리\n"
    class36 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 영B\n2교시: 기벡\n3교시: 한A\n4교시: 지학\n5교시: 창체\n6교시: 창체\n"
    class36 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class36 = sub + bar + classTime + bar + danger
#=============================class36end
#=============================class37
if t[r] == "월":
    classTime = "1교시: 한A\n2교시: 지학 \n3교시: 기백\n4교시: 진로\n5교시: 영B\n6교시: 법정\n7교시: 작A\n"
    class37 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 체육\n2교시: 생물\n3교시: 영A\n4교시: 기벡\n5교시: 한B\n6교시: 확통\n7교시: 작B\n"
    class37 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 작B\n2교시: 생물\n3교시: 기벡\n4교시: 한B\n5교시: 지학\n6교시: 영A\n"
    class37 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 영A\n2교시: 지학\n3교시: 기벡\n4교시: 작A\n5교시: 한A\n6교시: 생물\n7교시: 기벡\n"
    class37 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 확통\n2교시: 영B\n3교시: 체육\n4교시: 법정\n5교시: 창체\n6교시: 창체\n"
    class37 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class37 = sub + bar + classTime + bar + danger
#=============================class37end
#=============================class38
if t[r] == "월":
    classTime = "1교시: 체육\n2교시: 화학 \n3교시: 영B\n4교시: 작A\n5교시: 기벡\n6교시: 한A\n7교시: 진로\n"
    class38 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 기벡\n2교시: 생지\n3교시: 작A\n4교시: 한A\n5교시: 법정\n6교시: 영A\n7교시: 확통\n"
    class38 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 영A\n2교시: 생지\n3교시: 작B\n4교시: 확통\n5교시: 화학\n6교시: 기벡\n"
    class38 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 체육\n2교시: 화학\n3교시: 한B\n4교시: 영A\n5교시: 기벡\n6교시: 생지\n7교시: 작B\n"
    class38 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 기벡\n2교시: 한B\n3교시: 법정\n4교시: 영B\n5교시: 창체\n6교시: 창체\n"
    class38 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class38 = sub + bar + classTime + bar + danger
#=============================class38end
#==================================오늘의명언
#================================================오늘의명언end

def keyboard(request):

    return JsonResponse({
        'type':'buttons',
        'buttons':['오늘급식','선생님 위치 정보','시간표','오늘의명언','영등포고등학교 홈페이지','인성스포츠대회 경기일정','개발정보']
    })

@csrf_exempt
def message(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '오늘급식':

        return JsonResponse({
                'message': {
                    'text': '아래 중식, 석식중 선택하세요'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['중식','석식']
                }
            })

    elif datacontent == '처음으로':

        return JsonResponse({
                'message': {
                    'text': '처음으로'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','선생님 위치 정보','오늘의명언','시간표','영등포고등학교 홈페이지','인성스포츠대회 경기일정','개발정보']
                }
            })

    elif datacontent == '오늘의명언':

        return JsonResponse({
                'message': {
                    'text': '갈까 말까 할때는 가라\n살까 말까 할때는 사지마라\n말할까 말까 할때는 말하지 마라\n줄까 말까 할때는 줘라\n먹을까 말까 할때는 먹지마라'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '개발정보':

        return JsonResponse({
                'message': {
                    'text': '개발자 : 20612서정현,20521장환곤\n도움(프로오타러) : 김도유\n항상 조언해주시는 갓주현 선생님, 갓효진 선배\n>모두 감사드립니다.\n\n자세한정보 : https://github.com/rhaxlwo21/ydp_alarm_with_kakaoApi/tree/master'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '인성스포츠대회 경기일정':

        return JsonResponse({
                'message': {
                    'text': '현재 아직 인성스포츠대회 경기일정이 없습니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '영등포고등학교 홈페이지':

        return JsonResponse({
                'message': {
                    'text': '더 자세한 사항은 영등포고등학교 홈페이지를 참고하세요. \n홈페이지 주소 : http://www.ydp.hs.kr/index.do'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })


    elif datacontent == '시간표':

        return JsonResponse({
                'message': {
                    'text': '학년을 선택하세요.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['1학년','2학년','3학년']
                }
            })

    elif datacontent == '1학년':

        return JsonResponse({
                'message': {
                    'text': '반을 선택하세요.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['1학년1반','1학년2반','1학년3반','1학년4반','1학년5반','1학년6반','1학년7반','1학년8반']
                }
            })

    elif datacontent == '2학년':

        return JsonResponse({
                'message': {
                    'text': '반을 선택하세요.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['2학년1반','2학년2반','2학년3반','2학년4반','2학년5반','2학년6반','2학년7반','2학년8반']
                }
            })


    elif datacontent == '3학년':

        return JsonResponse({
                'message': {
                    'text': '반을 선택하세요.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['3학년1반','3학년2반','3학년3반','3학년4반','3학년5반','3학년6반','3학년7반','3학년8반']
                }
            })

    elif datacontent == '중식':

        return JsonResponse({
                'message': {
                    'text': mealM
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '석식':

        return JsonResponse({
                'message': {
                    'text': mealD
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })
            
    elif datacontent == '1학년1반':

        return JsonResponse({
                'message': {
                    'text': class11
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '1학년2반':

        return JsonResponse({
                'message': {
                    'text': class12
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '1학년3반':

        return JsonResponse({
                'message': {
                    'text': class13
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })
            
    elif datacontent == '1학년4반':

        return JsonResponse({
                'message': {
                    'text': class14
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '1학년5반':

        return JsonResponse({
                'message': {
                    'text': class15
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '1학년6반':

        return JsonResponse({
                'message': {
                    'text': class16
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })
            
    elif datacontent == '1학년7반':

        return JsonResponse({
                'message': {
                    'text': class17
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '1학년8반':

        return JsonResponse({
                'message': {
                    'text': class18
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '2학년1반':

        return JsonResponse({
                'message': {
                    'text': class21
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })
            
    elif datacontent == '2학년2반':

        return JsonResponse({
                'message': {
                    'text': class22
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '2학년3반':

        return JsonResponse({
                'message': {
                    'text': class23
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '2학년4반':

        return JsonResponse({
                'message': {
                    'text': class24
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '2학년5반':

        return JsonResponse({
                'message': {
                    'text': class25
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '2학년6반':

        return JsonResponse({
                'message': {
                    'text': class26
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '2학년7반':

        return JsonResponse({
                'message': {
                    'text': class27
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })
            
    elif datacontent == '2학년8반':

        return JsonResponse({
                'message': {
                    'text': class28
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '3학년1반':

        return JsonResponse({
                'message': {
                    'text': class31
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '3학년2반':

        return JsonResponse({
                'message': {
                    'text': class32
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })
            
    elif datacontent == '3학년3반':

        return JsonResponse({
                'message': {
                    'text': class33
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '3학년4반':

        return JsonResponse({
                'message': {
                    'text': class34
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '3학년5반':

        return JsonResponse({
                'message': {
                    'text': class35
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })
            
    elif datacontent == '3학년6반':

        return JsonResponse({
                'message': {
                    'text': class36
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '3학년7반':

        return JsonResponse({
                'message': {
                    'text': class37
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '3학년8반':

        return JsonResponse({
                'message': {
                    'text': class38
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '선생님 위치 정보':

        return JsonResponse({
                'message': {
                    'text': '찾고계신 선생님의 이름을 선택해주세요.\n(이름은 가나다순으로 정렬되어있습니다.) '
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['강우희 선생님','고경길 선생님','공지연 선생님','김경한 선생님','김민정 선생님','김보경 선생님','김서령 선생님','김수정 선생님','김은애 선생님','김주현 선생님','김지연 선생님','김창길 선생님','김흥일 선생님','권혜숙 선생님','나우철 선생님','나태영 교감선생님','나현경 선생님','남영남 선생님','류미진 선생님','박근배 선생님','박미옥 선생님','박민아 선생님','박베두루 선생님','박수현 선생님','박영갑 선생님','박원진 선생님','박점남 선생님','박종식 선생님','성순철 선생님','손민정 선생님','송 현 선생님','신나라 선생님','옥준석 선생님','우윤정 선생님','우주연 선생님','유호정 선생님','유안나 선생님','유완호 선생님','이준용 교장선생님','이연희 선생님','이주현 선생님','이동준 선생님','이상은 선생님','이원우 선생님','이은지 선생님','이미정 선생님','이상학 선생님','이선경 선생님','이정현 선생님','임정희 선생님','임정윤 선생님','전예슬 선생님','전지인 선생님','정정영 선생님','조인 선생님','최나리 선생님','하선종 선생님','하형숙 선생님','한은영 선생님','허호 선생님','홍일섭 선생님','홍임효 선생님']
                }
            })
	
    elif datacontent == '강우희 선생님':

        return JsonResponse({
                'message': {
                    'text': '강우희 선생님은 4층 복지상담부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '고경길 선생님':

        return JsonResponse({
                'message': {
                    'text': '고경길 선생님은 2층 안전생활부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '공지연 선생님':

        return JsonResponse({
                'message': {
                    'text': '공지연 선생님은 3층 창의인성교육부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '김경한 선생님':

        return JsonResponse({
                'message': {
                    'text': '김경한 선생님은 1층 교무기획부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '김민정 선생님':

        return JsonResponse({
                'message': {
                    'text': '김민정 선생님은 3층 2학년부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '김보경 선생님':

        return JsonResponse({
                'message': {
                    'text': '김보경 선생님은 4층 복지상담부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '김서령 선생님':

        return JsonResponse({
                'message': {
                    'text': '김서령 선생님은 1층 교육연구부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '김수정 선생님':

        return JsonResponse({
                'message': {
                    'text': '김수정 선생님은 1층 교육연구부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '김은애 선생님':

        return JsonResponse({
                'message': {
                    'text': '김은애 선생님은 3층 자연과학부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '김주현 선생님':

        return JsonResponse({
                'message': {
                    'text': '킹갓엠페러제너럴충무공마제스티목탁마스터 주현 선생님은 3층 안전생활부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '김지연 선생님':

        return JsonResponse({
                'message': {
                    'text': '김지연 선생님은 3층 창의인성고교육부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '김창길 선생님':

        return JsonResponse({
                'message': {
                    'text': '김창길 선생님은 4층 3학년부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '김흥일 선생님':

        return JsonResponse({
                'message': {
                    'text': '김흥일 선생님은 2층 안전생활부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '권혜숙 선생님':

        return JsonResponse({
                'message': {
                    'text': '권혜숙 선생님은 4층 복지상담부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })


    elif datacontent == '나우철 선생님':

        return JsonResponse({
                'message': {
                    'text': '나우철 선생님은 4층 3학년부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '나태영 교감선생님':

        return JsonResponse({
                'message': {
                    'text': '나태영 교감선생님은 1층 교무기획부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '나현경 선생님':

        return JsonResponse({
                'message': {
                    'text': '나현경 선생님은 2층 방송통신고 교무부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '남영남 선생님':

        return JsonResponse({
                'message': {
                    'text': '남영남 선생님은 3층 도서실에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '류미진 선생님':

        return JsonResponse({
                'message': {
                    'text': '류미진(달마 견주님) 선생님은 2층 방송통신고 교무부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '박근배 선생님':

        return JsonResponse({
                'message': {
                    'text': '박근배 선생님은 1층 행정실에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '박미옥 선생님':

        return JsonResponse({
                'message': {
                    'text': '박미옥 선생님은 1층 교무실에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '박민아 선생님':

        return JsonResponse({
                'message': {
                    'text': '박민아 선생님은 3층 자연과학부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '박베두루 선생님':

        return JsonResponse({
                'message': {
                    'text': '박베두루 선생님은 3층 스마트교육부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '박수현 선생님':

        return JsonResponse({
                'message': {
                    'text': '박수현 선생님은 1층 교무실에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '박영갑 선생님':

        return JsonResponse({
                'message': {
                    'text': '박영갑 선생님은 2층 1학년부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '박원진 선생님':

        return JsonResponse({
                'message': {
                    'text': '박원진 선생님은 2층 방송통신부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '박점남 선생님':

        return JsonResponse({
                'message': {
                    'text': '박점남 선생님은 2층 안전생활부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '박종식 선생님':

        return JsonResponse({
                'message': {
                    'text': '박종식 선생님은 1층 체육건강교육부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '성순철 선생님':

        return JsonResponse({
                'message': {
                    'text': '성순철 선생님은 2층 정보통신고 정보부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '손민정 선생님':

        return JsonResponse({
                'message': {
                    'text': '손민정 선생님은 1층 교무실 정보부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })
          
    elif datacontent == '송 현 선생님':

        return JsonResponse({
                'message': {
                    'text': '송 현 선생님은 4층 복지상담부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '신나라 선생님':

        return JsonResponse({
                'message': {
                    'text': '신나라 선생님은 3층 자연과학교육부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })


#ㅗ:옥준석
#ㅜ:우윤정,우주연, 
#ㅠ:유호정,유안나,유완호,
#ㅣ:이준용,이연희,이주현,이동준,이상은,이원우,#이은지,이미정,이상학,이선경,이정현, 임정희,#임정윤


    elif datacontent == '옥준석 선생님':

        return JsonResponse({
                'message': {
                    'text': '옥준석 선생님은 2층 1학년부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '우윤정 선생님':

        return JsonResponse({
                'message': {
                    'text': '우윤정 선생님은 2층 안정생활부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '우주연 선생님':

        return JsonResponse({
                'message': {
                    'text': '우주연 선생님은 1층 교무실에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '유완호 선생님':

        return JsonResponse({
                'message': {
                    'text': '유완호 선생님은 4층 3학년부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '유안나 선생님':

        return JsonResponse({
                'message': {
                    'text': '유안나 선생님은 2층 1학년부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '유호정 선생님':

        return JsonResponse({
                'message': {
                    'text': '유호정 선생님은 2층 안전생활부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })


    elif datacontent == '유호정 선생님':

        return JsonResponse({
                'message': {
                    'text': '유호정 선생님은 2층 안전생활부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '이동준 선생님':

        return JsonResponse({
                'message': {
                    'text': '이동준 선생님은 3층 창의인성교육부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })


    elif datacontent == '이미정 선생님':

        return JsonResponse({
                'message': {
                    'text': '킹갓엠페러제너럴충무공마제스티생명과학마스터 이미정 선생님은 3층 자연과학교육부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '이상은 선생님':

        return JsonResponse({
                'message': {
                    'text': '이상은 선생님은 3층 스마트교육부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '이상학 선생님':

        return JsonResponse({
                'message': {
                    'text': '이상학 선생님은 3층 2학년-방과후부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '이선경 선생님':

        return JsonResponse({
                'message': {
                    'text': '이선경 선생님은 3층 2학년-방과후부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '이연희 선생님':

        return JsonResponse({
                'message': {
                    'text': '이연희 선생님은 1층 교무실에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '이원우 선생님':

        return JsonResponse({
                'message': {
                    'text': '이원우 선생님은 3층 복지상담부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '이은지 선생님':

        return JsonResponse({
                'message': {
                    'text': '킹갓엠페러제너럴충무공마제스티아티스트 이은지 선생님은 2층 방송통신고 정보부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '이정현 선생님':

        return JsonResponse({
                'message': {
                    'text': '이정현 선생님은 3층 2학년-방과후부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })


    elif datacontent == '이주현 선생님':

        return JsonResponse({
                'message': {
                    'text': '이주현 선생님은 3층 창의인성교육부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '이준용 교장선생님':

        return JsonResponse({
                'message': {
                    'text': '이준용 교장선생님은 1층 교장실에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '임정윤 선생님':

        return JsonResponse({
                'message': {
                    'text': '육아 화이팅!!'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '전예슬 선생님':

        return JsonResponse({
                'message': {
                    'text': '전예슬 선생님은 3층 자연과학교육부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '전지인 선생님':

        return JsonResponse({
                'message': {
                    'text': '전지인 선생님은 1층 체육건강교육부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '정정영 선생님':

        return JsonResponse({
                'message': {
                    'text': '정정영 선생님은 1층 교무실에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '조인 선생님':

        return JsonResponse({
                'message': {
                    'text': '조인 선생님은 1층 체육건강교육부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '최나리 선생님':

        return JsonResponse({
                'message': {
                    'text': '최나리 선생님은 1층 교무실에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '하선종 선생님':

        return JsonResponse({
                'message': {
                    'text': '하선종 선생님은 4층 복지상담부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '하형숙 선생님':

        return JsonResponse({
                'message': {
                    'text': '하형숙 선생님은 1층 교무실에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '한은영 선생님':

        return JsonResponse({
                'message': {
                    'text': '한은영 선생님은 4층 복지상담부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '허호 선생님':

        return JsonResponse({
                'message': {
                    'text': '허호 선생님은 4층 복지상담부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '홍일섭 선생님':

        return JsonResponse({
                'message': {
                    'text': '홍일섭 선생님은 4층 복지상담부에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '홍임효 선생님':

        return JsonResponse({
                'message': {
                    'text': '홍임효 선생님은 1층 교무실에 계십니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })
