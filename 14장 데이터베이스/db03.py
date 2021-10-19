# db03.py 
import sqlite3

#연결객체 생성(임시로 메모리에 저장)
con = sqlite3.connect(":memory:")
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
for row in cur:
    print(row)

#백업받기
f = open("c:\\work\\dump.sql", "wt")
for item in con.iterdump():
    print(item)
    f.write(item + "\n")

f.close()

