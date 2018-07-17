Numbers = 10 #global space
def increment():
    global Numbers
    Numbers+=1 #local space
    print (Numbers)
    return
increment()
increment()
increment()
