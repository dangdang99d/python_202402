import random

n =int(input("정수를 입력하세요:"))
sum=0
kk =random.randint(0,10)
while True:
    num1 =int(input("정수를 입력하세요:"))
    if num1 ==n:
        break
    elif kk ==num1:
        break
    else:
        print("다시 입력:")
print("정답")







