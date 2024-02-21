# Circle  클래스
# 반지름 속성
# 원의 넓이, 원의 둘레 함수

class Circle:
    def __init__(self,a):
        self.round=a
        self.area=a
        self.cir=a
    def aa(self,a):
        self.area=a**2*3.24
        print(f"원의 넓이는 :{self.area}")
    def round(self,a):
        self.cir=a*2*3.24
        print(f"원의 둘레는 {self.cir}")
