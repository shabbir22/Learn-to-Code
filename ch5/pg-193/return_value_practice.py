#Greeting Return Function

def make_greetings(name):
    return "Hi "+name+'!'

greetings=make_greetings('Speedy')
print(greetings)

#Hi Speedy

#We can simply print a return value this way for a single value
print(make_greetings('Speedy'))

#Same output: Hi Speedy

#Compute Return Function

def compute(x,y):
    total=x+y
    if (total>10):
        total=10
    return total

print(compute(2,3))   ##Cause we already have a variable to store within the function named 'total'

#Output: 5

print(compute(11,3))

#Output: 10

#Allowing access

def allow_access(person):
    if person == 'Dr Evil':
        answer = True
    else:
        answer = False

    return answer

print(allow_access('Codie')) #Cause we already have a variable to store within the function named 'answer'

#Output: False

print(allow_access('Dr Evil'))

#Output: True
