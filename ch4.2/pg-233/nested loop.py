#Nested Loop Practice:
for i in range(0,4):   #outer loop   0,1,2,3
    for j in range(0,4):     #inner loop    0,1,2,3
        print(i * j)


for word in ['ox', 'cat', 'lion', 'tiger', 'bobcat']:   #outer loop   2,3,4,5,6 (length of the words)
    for i in range(2, 7):      #inner loop  2,3,4,5,6
        letters = len(word)
        if (letters % i) == 0:
            print(i, word)


full = False
donations = []
full_load = 45
toys = ['robot', 'doll', 'ball', 'slinky']

while not full:    #Outer Loop  #While not False
    for toy in toys:     #Inner Loop
        donations.append(toy)         #For each outer loop, i.e until the while statement is False, 4 toys are added to the 'donations' list each time, as there is 4 items in 'toys' list
        size = len(donations)
        if (size >= full_load):   #If this length of donations list is greater than equals to 45, full becomes True
            full = True            #Then it goes back to the Outer loop (while statement) and it become not True, i.e. False and the loop stopped

print('Full with', len(donations), 'toys')
print(donations)

