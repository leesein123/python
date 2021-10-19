def raiseErrorFunc():
    raise NameError

try:
    raiseErrorFunc()
except:
    print("NameErrir is Catched")

    
