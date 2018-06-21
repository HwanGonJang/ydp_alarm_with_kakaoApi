#3학년 6반 시간표를 if문으로 만들고 datetime 모듈로 자동으로 받아오도록 설정
import datetime

t = ['월','화','수','목','금','토','일',]
r = datetime.datetime.today().weekday()

sub = t[r] + "요일 시간표\n"
bar = "==========\n"
danger = "시간표가변경될수있습니다."

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
    
#print(class36)
