###which smoothies has coconut using for loop
smoothies=['coconut','strawberry','banana','tropical','acai berry']
has_coconut=[True,False,False,True,False]
length=len(has_coconut)

for i in range(length):
    if has_coconut[i]:     #If the expression is True i.e. if conditional expression finds True in has_coconut, it will go for print
        print(smoothies[i],'contains coconut') #For each iten created by the range, print smoothies of that index
