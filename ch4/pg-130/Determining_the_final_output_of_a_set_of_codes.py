eighties=['','duran duran','B-52s','muse']
newwave=['flock of seagulls','postal service']

remember=eighties[1]
eighties[1]='cultural club'

band=newwave[0]

eighties[3]=band
eighties[0]=eighties[2]
eighties[2]=remember

print(eighties)

length=len(eighties)  #Length of the list
print(length)   #4

#Obtaining the last item of the list eighties using the length of the list

eighties[len(eighties)-1]   #As we start numbering the indices of the list at zero, the length of the list will always be greater than one the last index

#Using the Negative Indices
eighties[-1]   #Will provide the last item of the list eighties

