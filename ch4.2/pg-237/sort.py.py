#Sorting the bubble scores in descending order and printing the top 5 solution's scores along with their number

def bubble_sort(scores,numbers):   #Defining the bubble_sort function with parameter 'scores' and 'numbers'
    swapped = True         #Setting a global variable 'swapped' to 'True'

    while swapped:         #Outer loop in the nested loop; The loop will continue as long as swapped is True
        swapped = False    # Initially setting swapped to False so that we can look for change
        for i in range(0, len(scores)-1):     #Inner loop with for loop; Range of index is less than 1 of the usual list as we used index i+1; else it would show unbound error
            if scores[i] < scores[i+1]:       #if False, skips the remaining statements and start with the next score
                temp = scores[i]              #If true [first item is less than the second item], scores [i] is saved to 'temp', a temporary variable, so that it can later be set to as scores [i+1]
                scores[i] = scores[i+1]       #Set scores [i] to scores [i+1], i.e. second item to first as it's the smaller one
                scores[i+1] = temp            #Set scores[i+1] to temp, i.e. first score to second one (scores [i+1])
                temp = numbers[i]             #We sort the numbers (parallel) list same as the scores list so that at the end each score number will be n the same relative position as its corresponding score 
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                swapped = True                #As swapping done, it's set to True; So need to proceed to next pass after looping through all the scores

scores = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]


solution_numbers = list(range(len(scores))) #Creating a paraller list ranges from 0 to length of scores


bubble_sort(scores, solution_numbers)   #Fethcing the arguments (the two parallel lists) into the bubble_sort definition
print (scores)
print (solution_numbers)
'''
print ('Top Bubble Solutions')
for i in range(0,5):
    print(str(i+1) + ')',
          'Bubble solution #'+str(solution_numbers [i]),
          'score:', scores [i])     #Top 5 solution's scores along with their number
'''
