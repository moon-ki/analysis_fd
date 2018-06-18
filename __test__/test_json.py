# test json
from urllib.request import Request, urlopen
from datetime import *
import sys
import json

try:
    url="http://kickscar.cafe24.com:8080/myapp-api/api/user/list"
    request = Request(url)
    resp = urlopen(request)

    # 문자열로 통신안하고 바이트 통신한다.
    resp_body = resp.read().decode("utf-8")
    print(type(resp_body),":",resp_body)        # 스트링의 형태

    # 이제 python의 json 라이브러리를 활용하여 파이썬에 있는 객체들로 변경하여 준다.
    # Java Script Object Notation : JSON
    #JSON의 장점은 여러 행태의 자료형으로 변경이 가능하다는 점이다.

    json_result = json.loads(resp_body)
    print(type(json_result),":",json_result)    #모양은 비슷하지만, 사전의 형태로 변환됨

    data = json_result['data']
    print(type(data),':',data)                  #이런식으로 가공이 용이하게 됨



except Exception as e:
    print( '%s %s' % (e,datetime.now()), file=sys.stderr ) #아무것도 안주면 디폴트는 file=sys.stdout 이다.

