from collect.api import api
from datetime import datetime, timedelta
import json

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

#Crawling!!
def crawling(page_name='', since='', until='',
             result_crawling_dir='' ,fetch='', access_token='', base_url='', limit_request=0,
             result_vidualization_dir=''):

    results=[]
    filename = '%s/fb_%s_%s_%s.json' % (result_crawling_dir, page_name, since, until)
    print('filepath:',filename)

    if fetch:
        # for year in range(start_year, end_year+1):
        #     for month in range(1,13):
        for posts in api.fb_fetch_posts(page_name, since, until, fetch,
                                        access_token, base_url, limit_request):
            for post in posts:
                preprocess_post(post)
            results+=posts
        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent=4,sort_keys=True, ensure_ascii=False)
            outfile.write(json_string)
            print('%s 파일 저장 완료' % (page_name))

    return filename