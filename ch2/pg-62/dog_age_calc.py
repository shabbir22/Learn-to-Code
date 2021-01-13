#Dog Age calculator

dog_name=input("What is your dog's name? ")     #Prompting the name of the dog from user
dog_age=int(input("What is your dog's age? "))       ##Prompting the age (chronological) of the dog from user, as well as converting the string input to integer

human_age=dog_age*7                         #converting dog age in human years

print('Your dog '+dog_name+' '+'is',human_age,'years old in human years')  #user friendly output

