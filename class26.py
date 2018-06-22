#2학년 6반 시간표를 if문으로 만들고 datetime 모듈로 자동으로 받아오도록 설정
import datetime

t = ['월','화','수','목','금','토','일',]
r = datetime.datetime.today().weekday()

sub = t[r] + "요일 시간표\n"
bar = "==========\n"
danger = "시간표가변경될수있습니다."

if t[r] == "월":
    classTime = "1교시: 물리\n2교시: 생물\n3교시: 미적\n4교시: 미술\n5교시: 영A\n6교시: 문A\n7교시: 문C\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1교시: 미적\n2교시: 영A\n3교시: 문B\n4교시: 일본어/중국어\n5교시: 체육A\n6교시: 진로\n7교시: 화학\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1교시: 지구과학\n2교시: 문A\n3교시: 물리\n4교시: 미술\n5교시: 일본어/중국어\n6교시: 미적A\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1교시: 체육\n2교시: 일본어/중국어\n3교시: 미적\n4교시: 영B\n5교시: 미적\n6교시: 지구과학\n7교시: 문B\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1교시: 미적\n2교시: 화학\n3교시: 생물\n4교시: 영A\n5교시: 창체\n6교시: 창체\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class26 = sub + bar + classTime + bar + danger
    
#print(class26)
