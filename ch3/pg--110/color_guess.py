#Modified the problem a bit

fav_color='green' #My favorite color
guess=''    #Empty String of other player's Color Guess
guesses=0   #Initially guesses set to zero

while guess!=fav_color:
    guess=input("What's my favorote color? ")
    guesses=guesses+1
if guesses==1:
    print("You've got me!",'It took you 1 guess.')
else:
    print("You've got me!",'It took you',guesses,'guesses')
