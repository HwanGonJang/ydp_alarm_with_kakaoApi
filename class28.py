#2학년 8반 시간표를 if문으로 만들고 datetime 모듈로 자동으로 받아오도록 설정
import datetime

t = ['월','화','수','목','금','토','일',]
r = datetime.datetime.today().weekday()

sub = t[r] + "요일 시간표\n"
bar = "==========\n"
danger = "시간표가변경될수있습니다."

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
    classTime = "1 교시:  영B\n2 교시:  문B\n3 교시:  화학\n4 교시:  미적\n5 교시:  실험\n6 교시:  실험\n7 교시:  진로\n"
    class28 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1 교시:  생물\n2 교시:  미적\n3 교시:  물리\n4 교시:  문A\n5 교시:  창체\n6 교시:  창체\n"
    class28 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class28 = sub + bar + classTime + bar + danger
    
#print(class28)
