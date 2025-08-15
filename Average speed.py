x=int(input('Please enter a number(integer).\n'))
y=int(input('Please enter another number(integer).\n'))
z=int(input('Please enter a third number(integer).\n'))
avg=(x+y+z)/3
print ('The average is equal to',avg,'.')
if avg>x and avg>y and avg>z:
    print(avg,'is greater than',x,',',y,'and',z,'.')
elif avg>x and avg>z:
    print(avg,'is greater than',x,'and',z,'.')
elif avg>x and avg>y:
    print(avg,'is greater than',x,'and',y,'.')
elif avg>y and avg>z:
    print(avg,'is greater than',y,'and',z,'.')
elif avg>x:
    print(avg,'is greater than',x,'.')
elif avg>y:
    print(avg,'is greater than',y,'.')
elif avg>z:
    print(avg,'is greater than',z,'.')
else:
    print ('Invalid Input')