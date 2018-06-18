# def squares(n=10):
#     result=[]
#     for i in range(n+1):
#         result.append(i++2)
#     return result

def squares(n=10):
    for i in range(n+1):
        yield i**2

for x in squares():
    print(x)