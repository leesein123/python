# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id #  변수 앞에 __ 를 붙이는 경우는 클래스의 변수 접근을 막기 위함...
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1) # accout1을 호출하면 class 에서 __str__ 를 찾는다...
#print(account1._BankAccount)  # 이렇게 호출하면 실행 안됨.
print(account1._BankAccount__balance)  # 이렇게 변수앞에 _클래스명__변수명으로 호출하면 됨..(백도어임..)
