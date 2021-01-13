###Obtaining the last item of a List

breakfast=['Bread','Butter','Banana','Water','Tea']
breakfast[len(breakfast)-1]  #We can directly call the last item of that list like this

#Conventional way:
length=len(breakfast)
last=breakfast[length-1] #Since the indexing of the list starts at 0
print(last)

#Using Negative Indices:
last=breakfast[-1]  #Calling the last item of the list
print(last)
