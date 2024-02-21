

class Restaurant:
    def __init__(self,a):
        self.name =a
        self.menu=[]
    def showMenu(self):
        print(f"메뉴: {self.menu}")
        
    def addMenu(self):
        food = input("추가 할 메뉴:")
        self.menu.append(food)
        

a= Restaurant("싸다 김밥")
a.addMenu()
a.addMenu()
a.addMenu()
b= Restaurant("이삭 토스트")

class Caffee:
    def __init__(self,a):
        self.name=a
        self.menu=[]
        self.worker=[]
        self.sum=0
    def add(self,a):
        name =input("커피 이름:")
        price=int(input("가격:"))
        self.menu.append({'name':name,'price':price})
    def hire(self,c):
        worker=input("직원 이름:")
        self.worker.append(worker)
    def showInfo(self):
        print(f"카페 이름:{self.name}  메뉴:{self.menu}")
    def sales(self):
        num=int(input(f"{self.menu}중에서 번호를 고르세요:"))
        self.sum +=self.menu[nim]['price']

        
t= Caffee("투썸")
t.add()
t.hire()
t.showInfo()
    
        
