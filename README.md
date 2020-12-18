# ydp_alarm_with_kakaoApi입니다.

이 폴더는 카카오톡 플러스 친구를 이용한 영등포고등학교 알람서비스인 ydpalarm에 사용된 것들입니다.
업데이트 정보를 확인하려면 patchNote를 확인하세요.

# ◎ 제공중인 서비스
1. 오늘의 급식
	- 중식
	- 석식
: 오늘의 급식을 '나이스'로부터 정보를 받아와 출력합니다
- url : http://stu.sen.go.kr/sts_sci_md01_001.do?

파서 출처 : M4ndU님 블로그, github
- github_url : https://github.com/M4ndU/school_meal_parser_python
- M4ndU'blog : http://mandu-mandu.tistory.com/category/Project/Programming

2. 오늘의 명언 (다음 업데이트에 오류수정 실패시 삭제될수 있습니다)
: 오늘의 명언을 naver로부터 정보를 받아와 출력합니다.
- url : https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blMy&query=%EA%B3%B5%EB%B6%80%20%EB%AA%85%EC%96%B8

4. 미세먼지-초미세먼지
: 미세먼지, 초미세먼지를 알려줍니다
- url : http://aqicn.org/city/korea/seoul/dongjak-gu/kr/

4. 개발정보
: 개발하기까지 참고한 사이트, 블로그 , 분들께 감사를 표하는 기능입니다.

5. 공지사항 버튼 추가
: 공지사항을 업로드. 

# ◎ 추가 예정인 기능
1. 없음

# ◎ 삭제된 기능
1. 스포츠 리그 일정표
: 스포츠 리그의 일정표 이미지로 출력합니다. ( 카카오톡 링크로, 사진 확대가 불가능합니다. 개선할 계획입니다.)
- 기상이변에 의한 지속적인 업로드 불가.
2. 시간표
: 오늘의 시간표를 출력합니다.

3. 선생님 위치 정보
: 선생님 교무실 위치를 보여줍니다.

# ◎ 파이썬 사용 모듈
- BeautifulSoup4
- regex
- datetime
- requests
- re
- random
- openurl

# ◎ ubuntu 사용 프로그램
- python
- apache
- Django
- venv

# ◎ 주로 사용한 ubuntu 명령어
- vi (문서편집기)
- cd (이동)
- sudo apachectl -k restart (아파치 재시작)
- crontab (시간이 UTC 0에 맞춰져 있어 crontab 사용시 주의, 단, 시간대를 조절할수 있음)
- mkdir (폴더 생성)
- cp (복사)
- touch (빈파일 생성)

# ◎ 서버
- Amazon Web Services Cloud

# ◎ 크롤링 오류 해결 헤더
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
headers = {'User-Agent':'Chrome/66.0.3359.181'}
headers = {'User-Agent':'Mozilla/5.0', 'referer' : 'http://www.naver.com'}
출처: http://napkingdom.tistory.com/10

# 겨우 남은 사진...
(사진좀 찍어놓을걸..)      
<img width="400" src="https://user-images.githubusercontent.com/33739448/102569288-845b3800-4128-11eb-9e03-03cb795de3d9.jpg">
<img width="400" src="https://user-images.githubusercontent.com/33739448/102569291-858c6500-4128-11eb-92eb-995cc4241c73.jpg">
<img width="400" src="https://user-images.githubusercontent.com/33739448/102569292-8624fb80-4128-11eb-8441-99325e40899f.jpg">
<img width="400" src="https://user-images.githubusercontent.com/33739448/102569504-f16ecd80-4128-11eb-919c-7c5d35796cff.jpg">



