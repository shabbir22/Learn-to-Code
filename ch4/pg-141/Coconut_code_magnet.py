###which smoothies has coconut
smoothies=['coconut','strawberry','banana','tropical','acai berry']
has_coconut=[True,False,False,True,False]

i=0
while i<len(has_coconut):
    if has_coconut[i]:     #If the expression is True i.e. if conditional expression finds True in has coconut it will go for print
        print(smoothies[i],'contains coconut') #For has_coconut True index, print smoothies of that index
    i=i+1


