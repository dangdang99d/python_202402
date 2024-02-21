class BankAccount:
    def __init__(self,a,b):                                                                           
        self.number =a
        self.name=b
        self.balance=0

    def deposit(self,a):
        self.balance +=a
        print("입금이 완료되었습니다.")
    def withdraw(self,a):
        if self.balance -a<0:
            print("출금 불가")
        else:
            self.balabce -=a
            print("출금 완료")

    def checkBalance(self):
        print(f"현재 남은 금액은 {self.balance}입니다.,")
                  
