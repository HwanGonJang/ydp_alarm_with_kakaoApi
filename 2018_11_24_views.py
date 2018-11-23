from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests, re
from bs4 import BeautifulSoup
import datetime
from urllib.request import urlopen, Request
import regex
import random
import urllib
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
#========================================오늘의급식end
#========================================명언
ranNum = random.randint(0,9)
wsurl_base = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blMy&query='
wsurl_mid = ['%EC%82%AC%EB%9E%91','%EC%9D%B8%EC%83%9D','%EA%B3%B5%EB%B6%80','%EC%84%B1%EA%B3%B5','%EC%B9%9C%EA%B5%AC','%EB%8F%85%EC%84%9C','%EC%9D%B4%EB%B3%84','%EC%8B%9C%EA%B0%84','%EB%85%B8%EB%A0%A5','%ED%9D%AC%EB%A7%9D','%EB%8F%84%EC%A0%84','%EC%9E%90%EC%8B%A0%EA%B0%90']
wsurl_tail = '%20%EB%AA%85%EC%96%B8'

url = wsurl_base + wsurl_mid[ranNum] + wsurl_tail
hdr = {'referer': wsurl_base + wsurl_mid[ranNum] + wsurl_tail, 'User-Agent':'Mozilla/5.0', 'referer' : 'http://www.naver.com'}
req = Request(url, headers=hdr)
page = urlopen(req)

wsSoup = BeautifulSoup(page,'html.parser')
wsText = wsSoup.find('p','lngkr').get_text()
wsMan = wsSoup.find('span','engnm').get_text()


var = '\n=========================\n'
wsTotal = '명언' + var + wsText + var + '          -' + wsMan + '-'
#========================================명언end
#========================================미세먼지, 초미세먼지
url_base = 'http://aqicn.org/city/korea/seoul/'
url_syb = 'dongjak-gu/kr/'

page = urlopen(url_base + url_syb)
soup = BeautifulSoup(page, 'html.parser')

pm25 = soup.find(id= 'cur_pm25').get_text()
pm10 = soup.find(id= 'cur_pm10').get_text()

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

resultpm25 = '동작구 초미세먼지: ' + pm25 + warning1 + '\n\nhttp://aqicn.org/city/korea/seoul/gwanak-gu/kr/ 에서 수집된 정보이고, 1시간 단위로 갱신되므로 정확하지 않을수 있습니다.'
resultpm10 = '동작구 미세먼지: ' + pm10 + warning2 + '\n\nhttp://aqicn.org/city/korea/seoul/gwanak-gu/kr/ 에서 수집된 정보이고, 1시간 단위로 갱신되므로 정확하지 않을수 있습니다.'
#========================================미세먼지, 초미세먼지end
#========================================시간표
sub = t[r] + "요일 시간표\n"
bar = "==========\n"
danger = "시간표가변경될수있습니다.\n오타제보 1대1 상담으로 부탁드립니다."
#========================================class기틀end
#========================================class17
if t[r] == "월":
    classTime = "1교시: 기술\n2교시: 기술\n3교시: 음악\n4교시: 국B\n5교시: 영B\n6교시: 한B\n7교시: 과A\n"
    class17 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 과B\n2교시: 통사\n3교시: 수학\n4교시: 과C\n5교시: 국A\n6교시: 진로\n7교시: 영A\n"
    class17 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 국B\n2교시: 수학\n3교시: 통사\n4교시: 한B\n5교시: 기술\n6교시: 기술\n"
    class17 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 한A\n2교시: 영A\n3교시: 수학\n4교시: 실험\n5교시: 체육\n6교시: 국B\n7교시: 과A\n"
    class17 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 통사\n2교시: 영B\n3교시: 미술\n4교시: 미술\n5교시: 창체\n6교시: 창체\n"
    class17 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class17 = sub + bar + classTime + bar + danger
#========================================class17end
#======================================class24
if t[r] == "월":
    classTime24 = "1교시: 미술\n2교시: 중어\n3교시: 진로\n4교시: 확통\n5교시: 영A\n6교시: 윤사\n7교시: 독A\n"
elif t[r] == "화":
    classTime24 = "1교시: 확통\n2교시: 세계\n3교시: 세지\n4교시: 생명\n5교시: 영A\n6교시: 중어\n7교시: 독B\n"
elif t[r] == "수":
    classTime24 = "1교시: 세지\n2교시: 중어\n3교시: 영A\n4교시: 독C\n5교시: 확통\n6교시: 체육\n"
elif t[r] == "목":
    classTime24 = "1교시: 체육\n2교시: 영B\n3교시: 윤사\n4교시: 환경\n5교시: 미술\n6교시: 독B\n7교시: 세계\n"
elif t[r] == "금":
    classTime24 = "1교시: 확통\n2교시: 독A\n3교시: 윤사\n4교시: 세지\n5교시: 창체\n6교시: 창체\n"
elif t[r] == "토" or "일":
    classTime24 = "토,일요일은 수업이 없습니다\n"
    
class24 = sub + bar + classTime24 + bar + danger
#=======================================class24end
#=================================class26
if t[r] == "월":
    classTime26 = "1교시: 생물\n2교시: 체육\n3교시: 화학\n4교시: 물리\n5교시: 독C\n6교시: 영A\n7교시: 확통\n"
elif t[r] == "화":
    classTime26 = "1교시: 영A\n2교시: 일중\n3교시: 지학\n4교시: 진로\n5교시: 미적\n6교시: 미적\n7교시: 독A\n"
elif t[r] == "수":
    classTime26 = "1교시: 체육\n2교시: 미술\n3교시: 확통\n4교시: 화학\n5교시: 일중\n6교시: 독A\n"
elif t[r] == "목":
    classTime26 = "1교시: 영A\n2교시: 일중\n3교시: 물리\n4교시: 미적\n5교시: 독B\n6교시: 영B\n7교시: 미술\n"
elif t[r] == "금":
    classTime26 = "1교시: 지학\n2교시: 생물\n3교시: 미적\n4교시: 독B\n5교시: 창체\n6교시: 창체\n"
elif t[r] == "토" or "일":
    classTime26 = "토,일요일은 수업이 없습니다\n"
    
class26 = sub + bar + classTime26 + bar + danger
#===============================class26end

def keyboard(request):

    return JsonResponse({
        'type':'buttons',
        'buttons':['급식','오늘의 명언','미세먼지-초미세먼지','시간표','영등포고등학교 홈페이지','변경사항','개발정보']
    })

@csrf_exempt
def message(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '급식':

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
                    'text': '메인페이지'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['급식','오늘의 명언','미세먼지-초미세먼지','시간표','영등포고등학교 홈페이지','변경사항','개발정보']
                }
            })

    elif datacontent == '오늘의 명언':

        return JsonResponse({
                'message': {
                    'text': wsTotal
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '시간표':

        return JsonResponse({
                'message': {
                    'text': '반을 선택하세요.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['1학년7반','2학년4반','2학년6반']
                }
            })

    elif datacontent == '개발정보':

        return JsonResponse({
                'message': {
                    'text': '개발자 : 20612서정현,20521장환곤\n인성스포츠 리그 권한 문제 해결 : 갓현석 선배\n오타300줄 : 김도유\n항상 조언해주시는 갓주현 선생님, 갓효진 선배,스포츠대회 일정 이미지 권한 문제 해결 유현석 선배님\n>모두 감사드립니다.\n\n명언 : NAVER에서 정보를 받아옴.\n급식: 나이스에서 받아옴\n시간표: 수제작\n\n자세한정보 : https://github.com/rhaxlwo21/ydp_alarm_with_kakaoApi/tree/master'
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

    elif datacontent == '변경사항':

        return JsonResponse({
                'message': {
                    'text': '선생님위치기능, 인성스포츠대회 일정(기상이변), 등 기능 삭제.\n초기 기획인 명언이 크롤링 오류 해결로 추가됨.\n\n2019년 5월말 혹은 6월초 금전적인 이유로 서비스 종료될 예정입니다 헣헣'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '미세먼지-초미세먼지':

        return JsonResponse({
                'message': {
                    'text': '선택하세요'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['미세먼지','초미세먼지']
                }
            })

    elif datacontent == '미세먼지':

        return JsonResponse({
                'message': {
                    'text': resultpm10
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '초미세먼지':

        return JsonResponse({
                'message': {
                    'text': resultpm25
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

