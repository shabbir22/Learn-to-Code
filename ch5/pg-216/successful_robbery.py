#success_robbery_from_bank

balance = 10500
camera_on = True

def steal(current_balance, amount):
    global camera_on
    camera_on = False
    global balance
    if (amount < balance):
        balance = balance - amount
    camera_on = True
    return amount
    
proceeds = steal(balance, 1250)
print('Criminal: you stole', proceeds)
print('Current balance is', balance)
print('Camera status is',camera_on)
