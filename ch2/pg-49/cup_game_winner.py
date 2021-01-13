#Cup game winner determiner

cup1=0
cup2=1
cup3=0

cup1=cup1+1
cup2=cup1-1
cup3=cup1

cup1=cup1*0
cup2=cup3
cup3=cup1

cup1=cup2%1
cup3=cup2

cup2=cup3-cup3

#Determing winner by showing which cup has 1
print(cup1)
print(cup2)
print(cup3)  #Has 1, hence the winner
