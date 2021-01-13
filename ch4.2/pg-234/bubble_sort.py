
#Sorting the bubble scores in ascending order

def bubble_sort(scores):   #Defining the bubble_sort function with parameter 'scores'
    swapped = True         #Setting a global variable 'swapped' to 'True'

    while swapped:         #Outer loop in the nested loop; The loop will continue as long as swapped is True
        swapped = False    # Initially setting swapped to False so that we can look for change
        for i in range(0, len(scores)-1):     #Inner loop with for loop; Range of index is less than 1 of the usual list as we used index i+1; else it would show unbound error
            if scores[i] > scores[i+1]:       #if False, skips the remaining statements and start with the next score
                temp = scores[i]              #If true [first item is greater than the second], scores [i] is saved to 'temp', a temporary variable, so that it can later be set to as scores [i+1]
                scores[i] = scores[i+1]       #Set scores [i] to scores [i+1], i.e. second item to first as it's the smaller one
                scores[i+1] = temp            #Set scores[i+1] to temp, i.e. first score to second one (scores [i+1])
                swapped = True                #As swapping done, it's set to True; So need to proceed to next pass after looping through all the scores


scores = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]

bubble_sort(scores)   #Fethcing the argument (scores list) into the bubble_sort definition
print(scores)         #printing the scores list in ascending order, i.e. smaller to larger


smoothies = ['coconut', 'strawberry', 'banana', 'pineapple']    #Another list of smoothies
bubble_sort(smoothies)  #Fetching smoothies list into bubble_sort function as argument
print(smoothies)        #Printing the smoothies list in alphabetical order


#Sorting the bubble scores in descending order

def bubble_sort(scores):   #Defining the bubble_sort function with parameter 'scores'
    swapped = True         #Setting a global variable 'swapped' to 'True'

    while swapped:         #Outer loop in the nested loop; The loop will continue as long as swapped is True
        swapped = False    # Initially setting swapped to False so that we can look for change
        for i in range(0, len(scores)-1):     #Inner loop with for loop; Range of index is less than 1 of the usual list as we used index i+1; else it would show unbound error
            if scores[i] < scores[i+1]:       #if False, skips the remaining statements and start with the next score
                temp = scores[i]              #If true [first item is greater than the second], scores [i] is saved to 'temp', a temporary variable, so that it can later be set to as scores [i+1]
                scores[i] = scores[i+1]       #Set scores [i+1] to scores [i], i.e. second item to first as it's the smaller one
                scores[i+1] = temp            #Set temp, i.e. first score to second one (scores [i+1])
                swapped = True                #As swapping done, it's set to True; So need to proceed to next pass after looping through all the scores

scores = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]

bubble_sort(scores)   #Fethcing the argument (scores list) into the bubble_sort definition
print(scores)         #printing the scores list in descending order

print('Bubble solution #' + str(i) + 'scores:',scores[i]) #Top 5 solution's scores along with their number

