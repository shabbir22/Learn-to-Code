#Sorting the bubble scores in descending order and printing the top 5 solution's scores along with their number using numpy module and built-in function

import numpy
scores = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]

sorted_index = numpy.argsort(scores)      #returning index of elements in sorted order in order to keep trace of the original index of the scores
print (sorted_index)

sorted_index_desc = sorted_index [::-1]   #Converting in descending order;      ::-1 means we choose all the elements, beginning with the last element in reverse order up to the very first element of the array.
print (sorted_index_desc)

'''
sorted_scores=numpy.sort(scores)
sorted_scores_desc=sorted_scores [::-1]   #::-1 means we choose all the elements, beginning with the last element in reverse order up to the very first element of the array.
print (sorted_scores_desc)

scores.sort(reverse = True)     #Sorting the original list of scores in descnding order

#print (scores)

#Printing the Top 5 solution's scores along with their number
print ('Top Bubble Solutions')
for i in range(0,5):
    print(str(i+1) + ')',
          'Bubble solution #'+str(sorted_index_desc [i]),
          'score:', scores [i]) 


'''
