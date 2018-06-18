from collect.api import api
from datetime import datetime, timedelta
import os
import json
RESULT_DIRECTORY='__results__/crawling'

#데이터 수집전 전처리
def preprocess_post(post):
    #공유수
    if 'shares' not in post:
        post['count_shares']=0
    else:
        post['count_shares']= post['shares']['count']

    #전체 리액션 수
    if 'rections' not in post:
            post['count_reactions']=0
    else:
        post['count_reactions']= post['reactions']['summary']['total_count']

    # 전체 코멘트 수
    if 'comments' not in post:
        post['count_comments'] = 0
    else:
        post['count_commentss'] = post['comments']['summary']['total_count']

   # KST = UTC + 9
    kst = datetime.strptime(post['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
    kst = kst + timedelta(hours=+9)
    post['created_time'] = kst.strftime('%Y-%m-%d %H:%M:%S')

def crawling(pageName, since, until,fetch):

    results=[]
    filename = '%s/fb_%s_%s_%s.json' % (RESULT_DIRECTORY, pageName, since, until)
    print('filepath:',filename)
    # filename = '%s/fb_%s_%s_%s.json' % (RESULT_DIRECTORY, pageName, since, untill)

    if fetch:
        for posts in api.fb_fetch_posts(pageName, since, until):
            for post in posts:
                preprocess_post(post)
                # print("preprocess_post(post): ",post)
            results+=posts
        # print('*************results',results)
        # print('============len(results):',len(results))
    #   save results to file (저장/적재)
        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent=4,sort_keys=True, ensure_ascii=False)
            outfile.write(json_string)

    return filename

if os.path.exists(RESULT_DIRECTORY) is False:
    print('create directory')
    os.makedirs(RESULT_DIRECTORY)
