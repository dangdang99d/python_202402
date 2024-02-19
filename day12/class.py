# 코드를 어떻게 짜면 좋은지 방법 중 하나
# pop[절차 지향 프로그래밍]: 옛날(무지성)
# oop[객체 지향 프로그래밍]: 조금 옛날(Class)
# fp[함수 지향 프로그래밍]: 트렌드(lambda)

# int, str, float, bool,list,dict -> 구조체[나만의 데이터 타입 명사느낌] + 함수(동작 느낌) = 클래스
class Student:
    def __init__(self):
        self.id=1
        self.major='computer'
        self.grade=1
    def studying(self):
        print('공부중')
    def Go(self):
        print('집가기')
class Dog:
    def __init__(self):
        self.name ='이름'
        self.breed ='시바'
        self.age=7
        self.gender='남'
    def taleWalking(self):
        print('산책중')

# 강아지 키우기 게임 클래스
class Dog:
    def __init__(self):
        self.hp=100
        self.skills=[]
        self.money=0

