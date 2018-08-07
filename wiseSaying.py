from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import random

ranNum = random.randint(0,9)
wsurl_base = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blMy&query='
wsurl_mid = ['%EC%82%AC%EB%9E%91','%EC%9D%B8%EC%83%9D','%EA%B3%B5%EB%B6%80','%EC%84%B1%EA%B3%B5','%EC%B9%9C%EA%B5%AC','%EB%8F%85%EC%84%9C','%EC%9D%B4%EB%B3%84','%EC%8B%9C%EA%B0%84','%EB%85%B8%EB%A0%A5','%ED%9D%AC%EB%A7%9D','%EB%8F%84%EC%A0%84','%EC%9E%90%EC%8B%A0%EA%B0%90']
wsurl_tail = '%20%EB%AA%85%EC%96%B8'

url = wsurl_base + wsurl_mid[ranNum] + wsurl_tail
hdr = {'referer': wsurl_base + wsurl_mid[ranNum] + wsurl_tail, 'User-Agent': 'Mozilla/5.0'}
req = Request(url, headers=hdr)
page = urlopen(req)

wsSoup = BeautifulSoup(page,'html.parser')
wsText = wsSoup.find('p','lngkr').get_text()
wsMan = wsSoup.find('span','engnm').get_text()


var = '\n=========================\n'
wsTotal = '오늘의 명언' + var + wsText + var + '          -' + wsMan + '-'
print(wsTotal)
