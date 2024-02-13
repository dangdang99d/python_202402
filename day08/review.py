for x in range(101):
    if(x%2==0):
        print(f"{x}")

u=int(input("정수를 입력하세요:"))
for x in range(9):
    print(f"{u} * {x} = {x*u}")

import random
k=[]
sum=0
for i in range(10):
    num1 =random.randint(1,10001)
    sum +=num1
    k.append(num1)

k.sort()
print(k)
print(sum) #혹은 sum()함수를 써도 된다.

