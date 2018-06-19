import os

CONFIG={
    'items':[{'page_name':'jtbcnews', 'since' : '2017-01-01', 'until': '2017-12-31'}
            ,{'page_name':'chosun','since' : '2017-01-01', 'until': '2017-12-31'}
             ],
    'common':{
        'result_crawling_dir':'__results__/crawling',
        'result_vidualization_dir':'__results__/visualization',
        'fetch':True,
        'access_token':'EAACEdEose0cBADZBJSj4nai17gqnuI8jZBEobcxZC60KtiZBZBBu5T4mbYhQfjs2M8AqNw5c9y7IexQfZBZBa9ZAjrGHaSN0n4VZB6wbJLDgjqgqwXDB2dbErPnyMXYeXvZA6UouR9LaGmsSEQahOsQZAj5t8imL3ExaJ56dVjz6SJmWT9RKEotza16Dy0o6ujHCZCkZD',
        'base_url':'https://graph.facebook.com/v3.0',
        'limit_request':50
    }
}

if os.path.exists(CONFIG['common']['result_crawling_dir']) is False:
    os.makedirs(CONFIG['common']['result_crawling_dir'])

if os.path.exists(CONFIG['common']['result_vidualization_dir']) is False:
    os.makedirs(CONFIG['common']['result_vidualization_dir'])