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

class25 = ""
class26 = ""
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
    classTime = "1 . 미적\n2. 화확\n3. 생물\n4. 영A\n5. 창체\n6. 창체\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class26 = sub + bar + classTime + bar + danger
#=================================class26end
#=================================class25
if t[r] == "월":
    classTime = "1교시:  영B\n2교시:  미적\n3교시:  체육\n4교시:  물리\n5교시:  문A\n6교시:  지구과학\n7교시:  진로\n"
    class25 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시:  영A\n2교시:  체육\n3교시: 문A\n4교시:  일본어/중국어\n5교시:  화학A\n6교시:  미적\n7교시:  미적\n"
    class25 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시:  생물\n2교시:  문B\n3교시:  지구과학\n4교시:  미적\n5교시:  일본어/중국어\n6교시:  미술\n"
    class25 = sub + bar + classTime + bar + danger
    elif t[r] == "목":
    classTime = "1 교시:  영A\n2 교시:  일본어/중국어\n3 교시:  미술\n4 교시:  화학\n5 교시:  생물\n6 교시:  문C\n7 교시:  미적\n"
    class25 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1 교시:  물리\n2 교시:  영A\n3 교시:  문B\n4 교시:  미적\n5 교시:  창체\n6 교시:  창체\n"
    class25 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class25 = sub + bar + classTime + bar + danger
#===============================class25end
#===============================class36
if t[r] == "월":
    classTime = "1교시:  확통\n2교시:  영A\n3교시:  물리\n4교시:  한A\n5교시:  작B\n6교시:  지학\n7교시:  기벡\n"
    class36 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시:  법정\n2교시:  물리\n3교시: 기벡\n4교시:  진로\n5교시:  작A\n6교시:  체육\n7교시:  영A\n"
    class36 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시:  지학\n2교시:  확통\n3교시:  영B\n4교시:  작B\n5교시:  기벡\n6교시:  한B\n"
    class36 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1 교시:  영A\n2 교시:  기벡\n3 교시:  법정\n4 교시:  한B\n5 교시:  체육\n6 교시:  작A\n7 교시:  물리\n"
    class36 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1 교시:  영B\n2 교시:  기벡\n3 교시:  한A\n4 교시:  지학\n5 교시:  창체\n6 교시:  창체\n"
    class36 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class36 = sub + bar + classTime + bar + danger

#=============================class36end

def keyboard(request):

    return JsonResponse({
        'type':'buttons',
        'buttons':['오늘급식','오늘의명언','시간표','개발하기까지']
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
                    'text': '시작이 반이다.\n가만히 있으면 반이라도 간다.\n시작하고 가만히 있자!!'
                },
                'keyboard': {
                    'type':'buttons',
                                        'buttons':['오늘급식','오늘의명언','시간표','개발하기까지']
                }

            })

    elif datacontent == '개발하기까지':

        return JsonResponse({
                'message': {
                    'text': '검색,구상,실현 : 서정현,장환곤\n항상 조언해주시는 : 갓주현쌤\n부스운영하러 오셔서 많은정보주신 효진이형\n>모두 감사드립니다.\n\n자세한정보 : https://github.com/rhaxlwo21/ydp_alarm_with_kakaoApi/tree/master'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','오늘의명언','시간표','개발하기까지']
                }
            })

    elif datacontent == '시간표':

        return JsonResponse({
                'message': {
                    'text': '학년,반을 선택하세요.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['2학년5반시간표','2학년6반시간표','3학년6반시간표','내 반도 추가하고싶다면?']
                }

            })

    elif datacontent == '처음으로':

        return JsonResponse({
                'message': {
                    'text': '처음으로'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','오늘의명언','시간표','개발하기까지']
                }

            })
    elif datacontent == '중식':

        return JsonResponse({
                'message': {
                    'text': mealM
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','오늘의명언','시간표','개발하기까지']
                }
            })


    elif datacontent == '석식':

        return JsonResponse({
                'message': {
                    'text': mealD
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','오늘의명언','시간표','개발하기까지']
                }
            })

    elif datacontent == '2학년5반시간표':

        return JsonResponse({
                'message': {
                    'text': class25
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','오늘의명언','시간표','개발하기까지']
                }
            })

    elif datacontent == '2학년6반시간표':

        return JsonResponse({
                'message': {
                    'text': class26
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','오늘의명언','시간표','개발하기까지']
                }
            })

    elif datacontent == '3학년6반시간표':

        return JsonResponse({
                'message': {
                    'text': class36
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','오늘의명언','시간표','개발하기까지']
                }
            })

    elif datacontent == '내 반도 추가하고싶다면?':

        return JsonResponse({
                'message': {
                    'text': '2학년5반 장환곤, 또는 2학년 6반 서정현에게 자신의 반의 시간표를 보내주세요.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘급식','오늘의명언','시간표','개발하기까지']
                }
            })
