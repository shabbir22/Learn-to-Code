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

solutions_with_high_score=[]     #Creating an empty list of 0 index to keep space for index of the bubble tests
for i in range(length):
    if high_score==scores[i]:    #Highest score will be matched to every item in scores
        solutions_with_high_score.append(i)   #If any item matched, then the index of that test will be added in solutions_with_high_scores
print('Bubble Solutions with the highest score:', solutions_with_high_score)  #Printing the index of the Bubble solutions which have highest score
        

#Testing the most cost effective (solution with the highest bubble score and lowest cost) solution
costs=[0.25,0.27,0.25,0.25,0.25,0.25,
       0.33,0.31,0.25,0.29,0.27,0.22,
       0.31,0.25,0.25,0.33,0.21,0.25,
       0.25,0.25,0.28,0.25,0.24,0.22,
       0.20,0.25,0.30,0.25,0.24,0.25,
       0.25,0.25,0.27,0.25,0.26,0.29]    #List of Bubble solution's costs

cost=100.0          #Setting 'cost' variable to 100, a higher value above the values in 'costs' list. For a much larger list needs to find out the highest value and set this above that value
most_effective=0    #Initially setting up the most effective solution index at 0
for i in range(length):
    if scores[i]==high_score and costs[i]<cost:  #Iterate over each solution; most_effective solution needs to have the highest score and a cost less the the previous solutions
        most_effective=i     #most effective solution's index
        cost=costs[i]       #most effective solution's cost
print('Solution #'+str(most_effective),'is the most effective one with a cost of',costs[most_effective])

#Alternative way of printing

print('Solution #'+str(most_effective),'is the most effective one with a cost of',cost)
