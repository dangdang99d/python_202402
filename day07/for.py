# for x in range(10):
#     print(x)
# # range(n): 0번부터 n번 반복해주는 기능
# # range(10,51): 10부터 50까지
# # a =[]
# # for x in range(100):
# #     a.append(x)
# # print(a)
import random

# a=[]
# for x in range(30):
#     a.append(random.randint(0,10000))
# print(a)

# a=[]
# # for x in range(101):
# #     if x%2==0:
# #         a.append(x)
# #
# # print(a)

# 3,5  최소공배수
# a=[]
# for x in range(0,101):
#     if x%3==0 and x%5==0:
#         a.append(x)
#
# print(a)

# for x in"megastudy":
#     print(x)
# for x in ['👨‍🦰','👨','asd']:
#     print(x)
y =int(input("정수 입력"))
print(f"{y}-->")
for x in range(1,10):
    print(f"{y}*{x} = {x*y}")

l=[]
import random
for x in range(10):
    l.append(random.randint(0,1000))
print(l)
a=0
for x in range(10):
    if l[x]%2==0:
        a = a+l[x]
print(f"짝수의 합은:{a}")

