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
#========================================명언
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import random

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
#========================================오늘의급식end

def keyboard(request):

    return JsonResponse({
        'type':'buttons',
        'buttons':['급식','명언','영등포고등학교 홈페이지','변경사항','개발정보']
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
                    'buttons':['급식','명언','영등포고등학교 홈페이지','변경사항','개발정보']
                }
            })

    elif datacontent == '명언':

        return JsonResponse({
                'message': {
                    'text': wsTotal
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

    elif datacontent == '개발정보':

        return JsonResponse({
                'message': {
                    'text': '개발자 : 20612서정현,20521장환곤\n인성스포츠 리그 권한 문제 해결 : 갓현석 선배\n오타300줄 : 김도유\n항상 조언해주시는 갓주현 선생님, 갓효진 선배,스포츠대회 일정 이미지 권한 문제 해결 유현석 선배님\n>모두 감사드립니다.\n\n자세한정보 : https://github.com/rhaxlwo21/ydp_alarm_with_kakaoApi/tree/master'
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
                    'text': '선생님위치기능, 인성스포츠대회 일정(기상이변), 등 기능 삭제.\n초기 기획인 명언이 크롤링 오류 해결로 추가됨.'
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['처음으로']
                }
            })

