import random       #importing the library 'random'
random_choice=random.randint(0,2)    #Randomly choose an integer between 0 and 2 and store it in the variable random_choice

if random_choice==0:      #Setting up "rock" as computer_choice variables value if random_choice=0 and so on for others two integers
    computer_choice='rock'
elif random_choice==1:
    computer_choice='paper'
else:
    computer_choice='scissors'

user_choice=''       #Creating an empty string
while (user_choice!='rock' and
       user_choice!='paper' and
       user_choice!='scissors'):
    user_choice=input('rock,paper or scissors? ')      #If users input anything other that 'rock','paper', or 'scissors', then keep prompting

winner=''           #Creating an empty string
if computer_choice==user_choice:       #If computer and user's choice matches, then winner will be called 'Tie'
    winner='Tie'
elif computer_choice=='paper' and user_choice=='rock':     #But for these 3 conditions, computer will be chosen winner
    winner='Computer'
elif computer_choice=='rock' and user_choice=='scissors':
    winner='Computer'
elif computer_choice=='scissors' and user_choice=='paper':
    winner='Computer'
else:
    winner='User'     #Other than that, user will be chosen winner

# For printing purpose at this stage add: print ('The',winner+', wins!')

if winner=='Tie':
    print('Match Tied!','We both chose',user_choice+'.'+" Let's Play Again.")
else:
    print (winner,'won!'+'; Computer chose',computer_choice+'.')


#If we didn't used the while loop to keep prompting the user when the user entered something else apart from 'rock', 'paper', 'scissors', the User will always win as the function won't find a match with the computer_choice and will return user as the winner all the time
#Can we give the liberty of case insensitive input from the user? Yes, we can. In another program using the upper() or lower() function.
    

    
