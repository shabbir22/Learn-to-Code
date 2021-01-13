#Determining the most recent item (smoothie flavor) created

smoothies=['coconut','strawberry','banana','pineapple','acai berry']

#First way,
most_recent=smoothies[-1]   #USing the negative index number, which refers to the last item in that list
print(most_recent)        #Printing the most recent item created in that list

#Second Way

most_recent=len(smoothies)-1   #To create the index number to call to the most recent item created in the list
recent=smoothies[most_recent]
print(recent) #Printing the most recent item created in that list
