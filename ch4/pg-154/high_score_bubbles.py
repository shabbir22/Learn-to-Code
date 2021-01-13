###bubbles report updated using for loop instead of while loop

scores=[60,50,60,58,54,54,58,50,52,54,48,69,34,55,
        51,52,44,51,69,64,66,55,52,61,46,31,57,52,
        44,18,41,53,55,61,51,44]

high_score=0     #Creating a variable high_score and setting its to 0

length=len(scores)   #Finding the length of the list scores
for i in range(length):
    print('Bubble solution #'+str(i),'score:',scores[i])
    if scores[i]>high_score:         #checking if any score from scores is higher than high_score
        high_score=scores[i]         #And the highest score will be added to high_score

print('Bubbles tests:',length)     #Printing the length of Bubble Tests
print('Highest bubbles score:',high_score)  #Printing the highest score

solutions_with_high_score=''     #Creating an empty list to keep space for index of the bubble tests
for i in range(length):
    if high_score==scores[i]:    #Highest score will be matched to every item in scores
        solutions_with_high_score=[i]   #If any matched found, then the index of that test will be stored in solutions_with_high_scores

print(solutions_with_high_score)  #Printing the index of the Bubble solutions which have highest score
        

