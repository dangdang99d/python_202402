# # if
# num = int(input("정수 입력:"))
# if num>0:
#     print("양수입니다.")
# print("프로그램 끝")
#
#
#
# num =len(input("문자를 입력하세요"))
# if num>=10 :
#     print("문자가 너무 길어요!")
# print("프로그램 끝")
# num = input("문자를 입력하세요")
# if num[-1].isupper() and len(num)>=5:
#     print("프로그램 끝")


# num =int(input("수를 입력하세요"))
# if num%2==0:
#     print("짝수입니다.")
# else:
#     print("홀수 입니다.입니다.")
# alpha= len(input("알파벳을 입력하세요"))
# if alpha %2==0:
#     print("짝수입니다.")
# else:
#     print("홀수 입니다.입니다.")
# alpha = input("알파벳을 입력하세요")
# if alpha.isupper() :
#     print("대문자 입니다.")
# else:
#     print("소문자입니다.")
# print("끝")


#
# mat = int(input("수학 점수를 입력:"))
# if mat>=90:
#     print("A")
# elif mat >= 80:
#     print("B")
# elif mat >= 70:
#     print("C")
# else:
#     print("샷건")

#
# angle = int(input("0~180 각도를 입력:"))
# if angle ==180:
#     print("평각")
# elif angle> 90 :
#     print("둔각")
# elif angle ==90:
#     print("직각")
# else:
#     print("예각")
char = input("단어를 입력하세요:")
if len(char)%2 ==0:
    if char.count('a')>0:
        print("a를 포함되어있는 짝수 네요")
    else:
        print("a를 없는 짝수 네요")
