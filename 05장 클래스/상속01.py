#부모클래스
class Person(object): #기본은 생략 가능한 object 를 상속받음
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

#자식클래스
class Student(Person):#부모클래스를 상속 받음
    #기존 초기화 메소드를 덮어쓰기(override)
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber
        
        #자식클래스에서 초기화 하기보다..기존에 부모클래스에 있기 때문에 가졍다 쓴다
        Person.__init__(self,name,phoneNumber) 
        self.subject = subject
        self.studentID = studentID
    #재정의    
    def printInfo(self): #부모클래스에 없는 다른 printInfo를 override 함...덮어쓰기함..
        #print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
         print("Info(Name:{0}, Phone Number: {1}, subject : {2}, studentId : {3})".format(self.name, self.phoneNumber,self.subject,self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo() # 자식코드에 printInfo가 없어  이름,전화번호만 나옴..

# print(p.__dict__)
# print(s.__dict__)


