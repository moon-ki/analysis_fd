#http test
from urllib.request import Request, urlopen
from datetime import *
import sys

try:
    url="http://www.naverdd.com"
    request = Request(url)
    resp = urlopen(request)

    # 문자열로 통신안하고 바이트 통신한다.
    resp_body = resp.read().decode("utf-8")
    print(resp_body)
except Exception as e:
    print( '%s %s' % (e,datetime.now()), file=sys.stderr ) #아무것도 안주면 디폴트는 file=sys.stdout 이다.

