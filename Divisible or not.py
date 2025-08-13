x=int(input('Please enter a number (integer).\n'))
y=int(input('Please enter another number (integer).\n'))
if x%y==0:
 print(x,'is divisible by',y,'.')
if y%x==0:
 print(y,'is divisible by',x,'.')
else:
 print('These numbers are not divisible by each other.')