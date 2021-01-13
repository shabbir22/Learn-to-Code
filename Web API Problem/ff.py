
def printlocalA(a):   #'a' is local variable here
    a=a+25
    print('Local value of a=',a)


a=100
print('Global value of a=',a)
printlocalA(50)
print('Global value of a=',a)

'''

def printlocalA():
    print('Local value of a=',a)


a=100   #Global Variable
print('Global value of a=',a)
printlocalA()
print('Global value of a=',a)
'''
