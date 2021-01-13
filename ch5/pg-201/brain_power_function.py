#Brain Power: 
def drink_me(param):
    msg = 'Drinking ' + param + ' glass'
    print(msg)
    param = 'empty'
    

glass = 'full'
drink_me(glass)
print('The glass is', glass)

#Outputs are: Drinking full glass & The glass is full.
#We got this variables because of the scope of the variables, that is, where in the function varibales were located
