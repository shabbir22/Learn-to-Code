#Calling get attribute

def get_attribute(query, default):   #setting the parameters of the function that only change over codes
    question = query + ' [' + default + ']? '    #String concatenation; including the question(query) as well as the default option
    answer = input(question)   #Prompting to the user for the response which will be stored in answer variable
    if (answer == ''):         #If the user pressed return key, then his answer will be assigned to default option
        answer = default
    print('You chose', answer)   #Printing the user choice
    return answer    # we need to get the answer to the code that called get_attribute.  If we don't use the return statement then nothing will be stored to the attributes (hair,eye,...). It will come as None
hair = get_attribute('What hair color', 'brown')  #Prompting user input; default is brown
hair_length = get_attribute('What hair length', 'short')
eye = get_attribute('What eye color', 'blue')
gender = get_attribute('What gender', 'female')
glasses = get_attribute('Has glasses', 'no')
beard = get_attribute('Has beard', 'no')
