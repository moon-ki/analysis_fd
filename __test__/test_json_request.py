from collect.api import web_request as wr

# url='http://kickscar.cafe24.com:8080/myapp-api/api/user/list'
# json_request= wr.json_request(url)
# print(json_request)

def success_fetch_user_list(response):
    print(response)

def error_fetch_user_list(e):
    print("사용자 에러발생1111")
    print(e)

wr.json_request(url="http://kickscar.cafe24.com:8080/myapp-api/api/user/list",
                success = success_fetch_user_list,
                error=error_fetch_user_list)
