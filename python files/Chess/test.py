def fun1():
    lis1=[]
    for i in range(5):
        fun2(lis1,i)
        print lis1
def fun2(lis,i):
    
        lis.append(i)
fun1()
    

