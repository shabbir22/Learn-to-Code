def greet(name,emoticon, message='You rule!'): #required parameter follows the default parameters
    print('Hi', name + '.', message, emoticon)

#SyntaxError:non-default argument follows the default arguments

def greet(name,emoticon, message='You rule!'): #default parameter follows the non-default parameters
    print('Hi', name + '.', message, emoticon)

greet('Rossi','happy for you!') #Keeping the default value for 'message' argument

#Output: Hi Rossi. You rule! happy for you!

#Using arguments with keywords

greet(message='How have you been?', name='Summer', emoticon='thumbs up') #using keywords with parameters name so that we can put arguments in any order. But if there is any required arguments, then we need to insert that before keyword argument

#But if we provide any required argument in the middle or or in the last, then it would show positional error
greet(message='How have you been?','Summer', emoticon='thumbs up')

#Mixing and matching positional and keyword argument #putting the required argument at first

greet('Betty', message='Yo!', emoticon=':)')   #Betty is posional arguments of the parameter name; but the remaining two are keyword arguments



