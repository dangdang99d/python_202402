class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model =model
    def display_info(self):
        print(f"브랜드: {self.brand} 모델: {self.model}")
class Car(Vehicle):
    def __init__(self,brand,model,engine):
        super().__init__(brand,model)
        self.engine =engine
    def info(self):
        self.display_info()
        print(f"engine:{self.engine}")

a=Car("밴츠","e클래스","v8")
a.info()


# 몬스터 클래스
# 체력, 공격력
# 떄리기

class Monster:
    def __init__(self,hp,at):
        self.hp=hp
        self.at=at
        self.skill ="때리기"
    def dispaly_mon(self):
        print(f"체력: {self.hp} 공격력: {self.at}")
    def hit(self):
        print(f"{self.attack} 데미지 입힙니다.")
# 메이플스토리 slime: 방어하기 추가  ,pig: 돌진하기 함수[공격력 2배], wraith: 속성 분노, 분노하기 함수[분노가오름], 급발진함수[공격력의 5배]
class Slime(Monster):
    def __init__(self,hp,at):
        super().__init__(hp,at)
    def defense(self):
        print("체력 안깎임")
class Pig(Monster):
    def __init__(self,hp,at):
        super().__init__(hp,at)
    def rush(self):
        print(f"공격력 {self.at*2}")
class Wraith(Monster):
    def __init__(self,hp,at):
        super().__init__(hp,at)
        self.rage=0
    def raiseRage(self):
        se;f.rage+=10
    def suddenRage(self):
        print(f"분노! 공격력 {self.at*5}입힘")
