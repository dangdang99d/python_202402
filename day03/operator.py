# operator
# 토큰[token]
# - +,-, *,/,//,**,% 수의 연산자
# 연결 연산자 : + [문자] 즉 문자 일떄
# 숫자 일떄 +를 쓰면 수의 연산자를 부르는 것이고 문자일떄는 연결 연산자를 부른다.
# 반복 연산자: * [문자]
# 비교 연산자: >, <, <=, ==[같다], !=[다르다]
# 대입 연산자 : =
# 비교 연산자의 결과 타입은 bool로 나옴
# print("넘 졸림"*5)
# print(5 > 3)
# print(f"10>5 : {10 >5}")
#
# num =1
# name = "메가짱"
# num = num + 5 # 갱신 느낌
# num += 10 # 축약버젼 -=, *=, /=



# 논리 연산자 : and, or, not
# and: 그리고, 교집합 : 모든 조건이 참인 경우 True
# or 또는 합집합
# not : bool결과 반대로

# print(10 >5 and 5 >1)
# print(not True)
# print(not bool(0))
# print(True and False)

# 멤버쉽 연산자: in 타게킹은 문자열이지만 결과는 bool값
print("mega" in "megastudy")
print("mega" not in "megastudy")

# 그룹핑 연산자()
print((3+2+1)/3)

#슬라이싱 연산자 타게팅[문자열] [start:end:step]
print("megastudy"[0:5])#megas
print("megastudy"[5]) #위와 같은 결과 [5],[:5],[0:5]
print("megastudy"[0:5:2]) #mgs
print("megastudy"[::2]) #처음부터 끝까지 2칸씩

# 인덱싱 연산자:[]
print("coffee"[1])



