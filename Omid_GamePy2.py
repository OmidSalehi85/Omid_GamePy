import random
a = random.randint(1,99)
b = random.randint(1,99)
jam = a + b
menha = a - b  
zarb = a * b
taghsim = a / b
print('                                             **welcome to Omid_GamePy2**  ')
name = input('What is your name? ')
ala = input('****Choose one of the math symbols to start the game(+,-,*,/): ')
print('   ')
if ala == '+':
   print('Q:',a,'+',b,'= ?') 
   j = input('Answer: ')    
   j =  int(j)
   while j != jam:
     print('False!!')
     j = input('Answer again: ')    
     j =  int(j)        
elif ala == '-':
    print('Q:',a,'-',b,'= ?')
    j = input('Answer: ')    
    j =  int(j)
    while j != menha:
      print('False!!')
      j = input('Answer again: ')    
      j =  int(j)
elif ala == '*':
    print('Q:',a,'*',b,'= ?')
    j = input('Answer: ')    
    j =  int(j)
    while j != zarb:
      print('False!!')
      j = input('Answer again: ')    
      j =  int(j)
elif ala == '/':
    print('Q:',a,'/',b,'= ?')
    j = input('Answer: ')    
    j =  int(j)
    while j != taghsim:
      print('False!!')
      j = input('Answer again: ')    
      j =  int(j)
print('   ')
print('****************Good job',name,'!!  You did it!!!!****************')
print('   ')
print('   ')
na = input(' Do you like "Omid_GamePy2"?(yes/no)  ')
if na == 'yes':
  print('##Thank you',name,' for supporting us.')
else:
  print('##Ok',name,', we are trying to make the game better.')