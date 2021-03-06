#Computing Read Ease Score of Text from Chapter 1

import ch1text              #a module which contains the texts by saving it the 'text' variable name ; should be saved in the same directory as analyze.py

def count_syllables(words):
    count = 0
    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count
    return count

def count_syllables_in_word (word): #defining another function within the function count_syllables to count the syllables in each word
    count = 0
 
    punctuation = '.,;!?:)("'          #Let's set up a string that contains all the word endings; double quotes are also added to remove it from the words
    last_char = word[-1]         #And get the last character of thecurrent word
    first_char = word[0]         #To remove the double quotes that are at the beginning of words
    
    if last_char in punctuation:          #Then check to see if the last character is one of the endings
        processed_word = word[0:-1]       #If so, we'll set the processed_word to be the word, without the last character [also solving the problem of double quotes]
    elif first_char in punctuation:         #Checking to see if the first character is one of the endings [double quote]
        processed_word = word[1:]           #If so, we'll set the processed_word to be the word, without the first character ["]
    else:
        processed_word = word             #If not, we're going to set the processed_word to the entire word
    
    if len(processed_word) <= 3 or 'walked' in processed_word:      #Checking if 'walked' is in the processed words or not, also if the length of the words are less that or equals to 3 or not
        return 1                  #If so, it will return only one syllable. It was perfomed because 'walked' has a single syllable.

    if processed_word[-1] in 'eE':               
        processed_word = processed_word[0:-1]    #We've put the code to remove silent 'e' characters here
        

    vowels = "aeiouAEIOU"            #First we're going to create a local variable, vowels, that holds all the vowels, lower- and uppercase
    prev_char_was_vowel = False      #First, we’re going to add a new local variable called prev_char_was_vowel, and set it to False.
    
    for char in processed_word:      #Our code is going to iterate over eachcharacter in a word
        if char in vowels:           #And we’re going to test if the current character is in the vowels string
            if not prev_char_was_vowel:     #If the current character is a vowel, and the previous character wasn’t, then increment the syllable count.
                count = count + 1
            prev_char_was_vowel = True      #In either case, we then set the prev_char_was_vowel to True before we process the next character
        else:
            prev_char_was_vowel = False     #If the current character isn’t a vowel, then we just set prev_char_was_vowel to False before we process the next character.


    if processed_word[-1] in 'yY':          #Check the word to see if it ends in y or Y, and if so, increase the syllable count
        count = count + 1
        
    return count                #Finally, we will return the total number of syllables accoss the word


def count_sentences(text):      #to count the number of terminal characters i.e. approximation of number of sentences
    count = 0

    terminals = '.;?!'          #Local variable holding all the terminal characters
    for char in text:           #To iterate through all the characterss in the string 'text'
        if char in terminals:   #if characters matches the terminals
        #if char == '.' or char == ';' or char == '?' or char == '!':
            count = count + 1
    return count                #Returning the count as the result of the function

def output_results (score):
    if score >= 90.0:
        print ('Reading level of 5th Grade')
    elif score >= 80.0:
        print ('Reading level of 6th Grade')
    elif score >= 70.0:
        print ('Reading level of 7th Grade')
    elif score >= 60.0:
        print ('Reading level of 8-9th Grade')
    elif score >= 50.0:
        print ('Reading level of 10-12th Grade')
    elif score >= 30.0:
        print ('Reading level of College Student')
    else:
        print ('Reading level of College Graduate')
        
def compute_readability(text):    #defining the function with parameter 'text'
    total_words = 0               #Local variables to hold values
    total_sentences = 0
    total_syllables = 0
    score = 0

    words = text.split()         #Split function to break down the text and put it up in a list as substrings
    total_words = len (words)    #lenght of that list, i.e. total number of words
    total_sentences = count_sentences (text)
    total_syllables = count_syllables (words)

    score = (206.835 - 1.015 * (total_words / total_sentences)
             - 84.6 * (total_syllables / total_words))             #reading ease score formula developed by US Navy

    #print (text)
    #print (words)
    #print ()                       #For a extra line to improve readability
    print (total_words, 'words')
    print (total_sentences, 'sentences')
    print (total_syllables, 'syllables')
    print('reading ease score is', score)
    output_results (score)           #passing the score to print the reading level of the text

compute_readability (ch1text.text)   #Invoking the function
