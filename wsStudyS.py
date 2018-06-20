#오늘의 명언을 naver에서 정보를 받아옴.
import urllib.request
import bs4

url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blMy&query=%EA%B3%B5%EB%B6%80%20%EB%AA%85%EC%96%B8"
html = urllib.request.urlopen(url)

a = "          오늘의 명언"
b = "================="
bsObj = bs4.BeautifulSoup(html, "html.parser")
wsStudy = bsObj.find("p",{"class":"lngkr"})
wsStudyE = bsObj.find("p",{"class":"lngeng"})
wsStudyP = bsObj.find("span",{"class":"engnm"})

wsStudy = str(wsStudy)
wsStudy = wsStudy.replace('</span>','')
wsStudy = wsStudy.replace('</p>','')
wsStudy = wsStudy.replace('<p class="lngkr">','')
wsStudy = wsStudy.replace('<span class="dot">','')
wsStudy = wsStudy.replace('<span class="dot cls">','')

wsStudyE = str(wsStudyE)
wsStudyE = wsStudyE.replace('</p>','')
wsStudyE = wsStudyE.replace('<p class="lngeng">','')

wsStudyP = str(wsStudyP)
wsStudyP = wsStudyP.replace('</span>','')
wsStudyP = wsStudyP.replace('<span class="engnm">','')

newstr = a+'\n'+b+'\n'+wsStudy+'\n'+wsStudyE+'\n'+"         by "+wsStudyP
print(newstr)
