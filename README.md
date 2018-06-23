# ydp_alarm_with_kakaoApi입니다.

이 폴더는 카카오톡 플러스 친구를 이용한 영등포고등학교 알람서비스인 ydpalarm에 사용된 코드들입니다.

◎ 제공중인 서비스
1. 오늘의 급식
	- 중식
	- 석식
: 오늘의 급식을 '나이스'로부터 정보를 받아와 출력합니다

url : http://stu.sen.go.kr/sts_sci_md01_001.do?

파서 출처 : M4ndU님 블로그, github

- github_url : https://github.com/M4ndU/school_meal_parser_python
- M4ndU'blog : http://mandu-mandu.tistory.com/category/Project/Programming

2. 오늘의 명언
: 오늘의 명언을 naver로부터 정보를 받아와 출력합니다. (오류가 나타나는 관계로 지금은 임시로 입력된 값이 출력됩니다.)

url : https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blMy&query=%EA%B3%B5%EB%B6%80%20%EB%AA%85%EC%96%B8

3. 시간표
: 오늘의 시간표를 출력합니다.
	- : 현재 시간표는 1학년, 2학년5반 ,6반 ,8반 , 3학년만 이용 가능합니다. 나머지는 구해지는 대로 추가하겠습니다.

4. 개발하기 까지
: 개발하기까지 참고한 사이트, 블로그 , 분들께 감사를 표하는 기능입니다.


◎ 추가 예정인 기능
1. 선생님 교무실 위치
: 선생님의 교무실 위치 알림 시스템을 추가할 예정입니다.

2. 스포츠 리그 일정표
: 스포츠 리그의 일정표를 표시할수 있도록 개발예정 입니다.

◎ 파이썬 사용 모듈
- BeautifulSoup4
- regex
- datetime
- requests
- re

◎ ubuntu 사용 프로그램
- python
- apache
- Django
◎ 사용한 ubuntu 명령어
- vi
- cd
- sudo apachectl -k restart
- crontab
- mkdir

◎ 서버
- Amazon Web Services Cloud
