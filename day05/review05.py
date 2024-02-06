num1 =int(input("0~99999입력:"))
print(f"{num1//10000}만{(num1%10000)//1000}천{(num1%1000)//100}백{(num1%100)//10}십{num1%10}",)

num2 =int(input("초 단위 정수를 입력하세요: "))
hour = num2 //3600
min = (num2%3600)//60
sec = num2 %60
print(f"{hour}:{min}:{sec}")

num3 =int(input("10000~99999 정수 입력"))
print(f"100의 자리 값:{(num3//100)%10}")
woon=[]
woon.append(input("사용자가 원하는 운동 종류 입력하세요:"))
woon.append(input("사용자가 원하는 운동 종류입력하세요:"))
woon.append(input("사용자가 원하는 운동 종류 입력하세요:"))
print(f"{woon[0]}->{woon[1]}->{woon[2]}")