from collect.api import api

# id = api.fb_name_to_id('jtbcnews')
# print(id)
i=0
posts = api.fb_fetch_posts('jtbcnews', '2017-01-01', '2017-12-31')
for post in posts:
    i+=1
    print('[',i,']: ',post)