import json
import re
from konlpy.tag import Twitter
from collections import Counter
# [a-zA-Z1-9]: a-z, A-Z, 1-9 까지의 모든 문자
# .*: 모든 문자
# [^\w]+: 공백문자로 시작하는 모든 문자들의 1개 이상(+없으면 1개의 문자)

def json_to_str(filename, key):
    jsonfile=open(filename, 'r',encoding='utf-8')

    #파일내용 읽기
    json_string = jsonfile.read()
    jsonfile.close()  # 해주어야 함

    #파이선 객체로 만듬
    json_data=json.loads(json_string)

    data=''
    for item in json_data:
        value = item.get('message')
        if value is None:
            continue
        data += re.sub(r'[^\w]','', value)     #value의 공백문자는 모두 ''로 대체하라
    return data

def count_wordfreq(data):
    twiter = Twitter()
    nouns = twiter.nouns(data)
    count = Counter(nouns)
    return count