characters=['t','a','c','o']

output=''   #Creating an empty string in the name of 'output'
length=len(characters)

i=0     #Loop starts at i=0
while (i<length):     #Run as long as the value of 'i' is less than length (4)
    output=output+characters[i]   #For True evaluation, adds an item from characters using the indices
    i=i+1             #For each True evaluation, adds 1 to 'i'

length=length*-1     #Multiply the length of characters by -1

i=-2       #Another Loop starts with -2
while(i>=length):    #Execute as long as 'i' greater than or equals to length, which is -4 in this case
    output=output+characters[i]
    i=i-1             #This time for each True evaluation, subtracts 1 form 'i'

print(output)  #'tacocat'


#Alternative character list
characters=['a','m','a','n','a','p','l','a','n','a','c']

output=''   #Creating an empty string in the name of 'output'
length=len(characters)

i=0     #Loop starts at i=0
while (i<length):     #Run as long as the value of 'i' is less than length (11)
    output=output+characters[i]   #For True evaluation, adds an item from characters using the indices
    i=i+1             #For each True evaluation, adds 1 to 'i'

length=length*-1     #Multiply the length of characters by -1

i=-2       #Another Loop starts with -2
while(i>=length):    #Execute as long as 'i' greater than or equals to length, which is -11 in this case
    output=output+characters[i]
    i=i-1             #This time for each True evaluation, subtracts 1 form 'i'

print(output)  #'amanaplanacanalpanama'


#Another alternative character list
characters=['w','a','s','i','t','a','r']

output=''   #Creating an empty string in the name of 'output'
length=len(characters)

i=0     #Loop starts at i=0
while (i<length):     #Run as long as the value of 'i' is less than length (7)
    output=output+characters[i]   #For True evaluation, adds an item from characters using the indices
    i=i+1             #For each True evaluation, adds 1 to 'i'

length=length*-1     #Multiply the length of characters by -1

i=-2       #Another Loop starts with -2
while(i>=length):    #Execute as long as 'i' greater than or equals to length, which is -7 in this case
    output=output+characters[i]
    i=i-1             #This time for each True evaluation, subtracts 1 form 'i'

print(output)  #'wasitaratisaw'
