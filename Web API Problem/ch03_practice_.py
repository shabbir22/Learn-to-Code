'''
if bank_balance >= ferrari_cost:
    print('Why not!\'Go ahead, buy it.')

#If we run this that way, we will get NameError, as bank_balance and ferrari_cost isn't defined yet
'''

bank_balance=20000
ferrari_cost=15000

if bank_balance >= ferrari_cost:   #Boolean expression with 'if' keyword
    print("Why not!\nGo ahead, buy it.") #Printing in two lines
#This will work
