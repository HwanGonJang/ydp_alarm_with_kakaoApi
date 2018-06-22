#0학년 0반 시간표를 if문으로 만들고 datetime 모듈로 자동으로 받아오도록 설정
import datetime

t = ['월','화','수','목','금','토','일',]
r = datetime.datetime.today().weekday()

sub = t[r] + "요일 시간표\n"
bar = "==========\n"
danger = "시간표가변경될수있습니다."

if t[r] == "월":
    classTime = "1 교시: @\n2교시: @\n3교시: @\n4교시: @\n5교시: @\n6교시: @\n7교시: @\n"
    class00 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1 교시: @\n2교시: @\n3교시: @\n4교시: @\n5교시: @\n6교시: @\n7교시: @\n"
    class00 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1 교시: @\n2교시: @\n3교시: @\n4교시: @\n5교시: @\n6교시: @\n"
    class00 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1 교시: @A\n2 교시: @\n3 교시: @\n4 교시: @\n5 교시: @\n6 교시: @\n7 교시: @\n"
    class00 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1 교시: @\n2 교시: @\n3 교시: @\n4 교시: @\n5 교시: @\n6 교시: @\n"
    class00 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class00 = sub + bar + classTime + bar + danger
    
#print(class00) #테스트용도
