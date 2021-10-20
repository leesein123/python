def divide(a,b):
    return a/b
try:
    result =divide(5,2)
   
except ZeroDivisionError:
    print("0으로 나눌수 없음")
except TypeError:
    print("숫자만 연산이 됩니다")
else:
    print ("결과 :{0}".format(result))
finally:
    print("무조건 실행")

print ("전체코드 실행")