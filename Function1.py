# Function1.py 
#키워드인자(파라메터명 명시)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL 

#호출
print( connectURI("credu.com", "80") )
print( connectURI(port="80", server="credu.com") )