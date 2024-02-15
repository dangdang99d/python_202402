# [내장[파이썬, 표준] 함수]: print().........input
# [문자열 함수] "ㅁㄴㅇㄹ".isupper()
#함수 정의
# def add(a,b):
#     c= a+b
#     return c
# # substract, multiply 함수
# def sbstract(a,b):
#     c= a*b
#     return c
# def makeTofry(a):
#     if(a=='🥚'):
#         b='🍳'
#     else:
#         b = '🍞🍞'
#     return b
# def bank(x):
#     if(x == "농협은행") :
#         k = "넘이쁘네"
#     elif x == "기업은행":
#         k = "궈ㅣ여운네"
#     elif x == "국민은행":
#         k = "고민해"
#     elif x == "신한은행":
#         k = "신나네"
#     else:
#         k='?'
#     return k

#가변 매개변수
# def makePizza(*topping):
#     for i in topping:
#         print(f"추가되는 토핑{i}")

# def zodiac(*x):
#     print("1996~2005")
#     jj = {
#         1996: "쥐띠",
#         1997:"소띠",
#         1998:"호랑이띠",
#         1999:"토끼",
#         2000:"용띠",
#         2001:"뱀띠",
#         2002:"양띠",
#         2003:"원숭이띠",
#         2004:"닭띠"
#
#
#
#     }
#
#     for i in x:
#         print(f"{i}는 {jj[i]}")
# zodiac(1997,1999)

def kk(n):
    n_st =str(n)
    u=list(n_st)
    u.reverse()  # 문자열이기 때문에 reverse의 역 의미가 문자 순서의 역으로 해석된다. 
    return u


print(kk(8937))




