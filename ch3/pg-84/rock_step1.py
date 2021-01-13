import random       #importing the library 'random'
random_choice=random.randint(0,2)    #Randomly choose an integer between 0 and 2 and store it in the variable random_choice

if random_choice==0:      #Setting up "rock" as computer_choice variables value if random_choice=0 and so on for others two integers
    computer_choice='rock'
elif random_choice==1:
    computer_choice='paper'
else:
    computer_choice='scissors'

print('The computer chooses',computer_choice)
