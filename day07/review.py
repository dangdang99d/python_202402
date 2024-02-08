alpha = input("문자 한 개를 입력해주세요!:")
if alpha.isupper():
    {
        print(alpha.lower())
    }
else:
    print(alpha.upper())


passs = input("10글자 비밀번호 입력해주세요!:")
if len(passs) <10:
    print("다시 10글자 이상 설정해주세요")
elif not("!" in passs or "#" in passs or "@" in passs):
    print("특수문자 생성해주세요")
elif not passs[0].isupper():
    print("첫 글자 대문자로 설정")
else:
    print("비밀번호 설정됨")
bus_fee ={
    'name':['시내버스','광역버스','마을버스'],
    'fee':[1200,2000,1000],
    'age_discount': ['어린이 무료','청소년 30%','노인 무료']
}
print(f"{bus_fee['name']} {bus_fee['fee']}  {bus_fee['age_discount']} ")


A=int(input("나이입력:"))
B=int(input("버스 입력 정수로"))
if(A<=7 or A>=65):
        print("무료")
else:
    print(f"{bus_fee['fee'][B]*0.7}")
