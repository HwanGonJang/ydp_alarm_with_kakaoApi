# ydpalarm 챗봇을 돌릴때 사용되는 ubuntu 서버에 /home/ubuntu/django/meal에 위치한 views.py파일의 내용입니다.

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
sub = t[r] + "요일 시간표\n"
bar = "==========\n"
danger = "시간표가변경될수있습니다."

if t[r] == "월":
    classTime = "1 . 물리\n2. 생물\n3. 미적\n4. 미술\n5. 영A\n6. 문A\n7. 문C\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1 . 미적\n2. 영A\n3. 문B\n4. 일본어/중국어\n5. 체육A\n6. 진로\n7. 화학\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1 . 지구과학\n2. 문A\n3. 물리\n4. 미술\n5. 일본어/중국어\n6. 미적A\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1 . 체육\n2. 일본어/중국어\n3. 미적\n4. 영B\n5. 미적\n6. 지구과학\n7. 문B\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1 . 미적\n2. 화학\n3. 생물\n4. 영A\n5. 창체\n6. 창체\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class26 = sub + bar + classTime + bar + danger
#=================================class26end

def keyboard(request):

    return JsonResponse({
        'type':'buttons',
        'buttons':['오늘급식','오늘의명언','2학년6반시간표','개발하기까지']
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

    elif datacontent == '오늘의명언':

        return JsonResponse({
                'message': {
                    'text': '환곤이 일했는데오류나요...'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','오늘의명언','2학년6반시간표','개발하기까지']
                }

            })

    elif datacontent == '개발하기까지':

        return JsonResponse({
                'message': {
                    'text': '검색,구상,실현 : 서정현,장환곤\n항상 조언해주시는 : 갓주현쌤\n부스운영하러 오셔서 많은정보주신 효진이형\n>모두 감사드립니다.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','오늘의명언','2학년6반시간표','개발하기까지']
                }
            })

    elif datacontent == '2학년6반시간표':

        return JsonResponse({
                'message': {
                    'text': class26
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','오늘의명언','2학년6반시간표','개발하기까지']
                }

            })

    elif datacontent == '처음으로':

        return JsonResponse({
                'message': {
                    'text': '처음으로'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','오늘의명언','2학년6반시간표','개발하기까지']
                }

            })
    elif datacontent == '중식':

        return JsonResponse({
                'message': {
                    'text': mealM
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','오늘의명언','2학년6반시간표','개발하기까지']
                }
            })


    elif datacontent == '석식':

        return JsonResponse({
                'message': {
                    'text': mealD
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','오늘의명언','2학년6반시간표','개발하기까지']
                }
            })
