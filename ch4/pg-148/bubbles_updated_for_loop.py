###bubbles report updated using for loop instead of while loop

scores=[60,50,60,58,54,54,58,50,52,54,48,69,34,55,
        51,52,44,51,69,64,66,55,52,61,46,31,57,52,
        44,18,41,53,55,61,51,44]
scores
length=len(scores)

for i in range(length):        #Performing the iteration for each item created by the range(length) sequence
    print('Bubble solution #'+str(i),'score:',scores[i]) 

