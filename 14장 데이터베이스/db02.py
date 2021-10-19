# db02.py 
import sqlite3
#연결객체 생성(영구적으로 파일로 저장)
con = sqlite3.connect("c:\\work\\sample.db")
#SQL구문을 실행할 커서 객체 리턴
cur = con.cursor()
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick','010');")
#파라메터로 입력 처리 
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))
#다중의 데이터를 입력
datalist = (("tom","010-123"), ("dsp","010-555"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#결과를 확인
cur.execute("select * from PhoneBook;")
print(cur.fetchall())
#커밋으로 작업을 완료
con.commit() 
