#2학년 5반 시간표를 if문으로 만들고 datetime 모듈로 자동으로 받아오도록 설정
import datetime

t = ['월','화','수','목','금','토','일',]
r = datetime.datetime.today().weekday()

sub = t[r] + "요일 시간표\n"
bar = "==========\n"
danger = "시간표가변경될수있습니다."

if t[r] == "월":
    classTime = "1 교시: 영B\n2교시: 미적\n3교시: 체육\n4교시: 물리\n5교시: 문A\n6교시: 지구과학\n7교시: 진로\n"
    class25 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1 교시: 영A\n2교시: 체육\n3교시: 문A\n4교시: 일본어/중국어\n5교시: 화학A\n6교시: 미적\n7교시: 미적\n"
    class25 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1 교시: 생물\n2교시: 문B\n3교시: 지구과학\n4교시: 미적\n5교시: 일본어/중국어\n6교시: 미술\n"
    class25 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1 교시: 영A\n2 교시: 일본어/중국어\n3 교시: 미술\n4 교시: 화학\n5 교시: 생물\n6 교시: 문C\n7 교시: 미적\n"
    class25 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1 교시: 물리\n2 교시: 영A\n3 교시: 문B\n4 교시: 미적\n5 교시: 창체\n6 교시: 창체\n"
    class25 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class25 = sub + bar + classTime + bar + danger
    
#print(class25)
