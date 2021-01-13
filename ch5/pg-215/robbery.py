#failed_robbery

balance=10500
camera_on = True
def steal(balance, amount):
    global camera_on
    camera_on = False
    if (amount < balance):
        balance = balance - amount   #Actual balance didn't change, as the global variable is shadowed by the parameter 'balance'
    return amount
    camera_on = True   #The criminal left the camera on but it will not go into the execution of the function as after return statement the function is executed

proceeds = steal(balance, 1250)
print('Criminal: you stole', proceeds)

#successful_robbery
camera_on = True
def steal(balance, amount):
    global camera_on
    camera_on = False
    if (amount < balance):
        balance = balance - amount
    camera_on = True
    return amount
    
proceeds = steal(10500, 1250)
print('Criminal: you stole', proceeds)

