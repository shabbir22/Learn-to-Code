def hook_fish ():
    print('I got a fish!')

#hook_fish()  #printing 'I got a fish'

def wait ():
    print('Waiting...')

print ('Get worm')
print ('Put worm on hook')
print ('Throw in lure')

while True:
    response=input('Is bobber underwater? ')   #It will create an infinite loop; If the response isn't 'yes' then it will show 'waiting' and keep promting
    if response=='yes':
        is_moving= True
        print('I got a bite!')
        hook_fish()
    else:
        wait()
