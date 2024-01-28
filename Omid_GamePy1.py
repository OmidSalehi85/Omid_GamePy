import random
j = random.randint(1,99)
print('                                           **welcome to Omid_GamePy**  ')
name = input('What is your name, my friend? ')

h = input('Enter your guess number? ')
h = int(h)

while h != j:
    if h < j:
        print('mine is bigger!')
    else:
        print('mine is smaller!')
    h = input('Enter your guess again? ')
    h = int(h)

print('WOWW!!  Good job %s!!  You did it!!!!' %name)
