#Rock, Paper, Scissors Game with computer giving user the liberty to give lower or upper case inputs

import random
choice=['rock','paper','scissors']
computer_choice=random.choice(choice)

user_choice=''
while (user_choice!='rock' and
       user_choice!='paper' and
       user_choice!='scissors'):
    user_choice=input('rock,paper or scissors? ')      #If users input anything other that 'rock','paper', or 'scissors', then keep prompting
    user_choice=user_choice.lower()  #converting in lower case to avoid case sensitivity

winner=''                       #Creating an empty string
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
