#FaceBook API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN='EAACEdEose0cBAFDtqtrh0I1FtF9ylpiQi0ZChDkiZCZA37GLCoi887YNvQAD1vl0JXnJU7M5jSenVYSNM9SGYMTaJmGFAT5dE9trjNHB0jbDpeKnTQqnKZCkiUZCdLFOPGqI2JvmIx4nlB1TtgClzTP1IPcOqXkKQERWSL6ANzr6098FtXxsIbfEFNZC2f7eQZD'
BASE_URL_FB_API = 'https://graph.facebook.com/v3.0/'
LIMIT_REQUEST = 50


def fb_gen_url(
        base=BASE_URL_FB_API,
        node='',
        **params):#딕셔너리형 가변인수
    return "%s/%s/?%s" % (base, node, urlencode(params))

#base/node/?access_token : id를 리턴하는 URL 포멧!!
def fb_name_to_id(pagename):
    url=fb_gen_url(node=pagename,
                   access_token=ACCESS_TOKEN)
    json_result=json_request(url=url)
    print('json_result:',json_result)
    return json_result.get('id')


def fb_fetch_posts(pageName, since, until):
    # print("api/fb_fetch_posts CALLED")
    url=fb_gen_url(node=fb_name_to_id(pageName)+"/posts",
                   fields = 'id, message, link, name, type, shares, created_time,\
                          reactions.limit(0).summary(true), comments.limit(0).summary(true)',
                   since = since,
                   until=until,
                   limit = LIMIT_REQUEST,
                   access_token=ACCESS_TOKEN)
    # json_result=json_request(url=url)

    isnext = True
    while isnext is True:
        json_result = json_request(url=url)                                     #json을 list 형태로 받아옴.
        paging = None if json_result is None else json_result.get('paging') #다음 페이지가 없으면 None
        posts  = None if json_result is None else json_result.get('data')   #다음페이지의 post

        url =  None if paging is None else paging.get('next')               #다음페이지 url
        isnext = url is not None

        yield posts