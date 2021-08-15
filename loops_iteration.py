print('loops and iteration')

print('1. while loop : infinite loop')
print('it will looping infinite as statements does not change each iteration')

n=0
while n<5:
    n=n+1
    print('n is still lower than 5')
print('done')

print('1-2. break can break loops')
b=0
while b<5:
    b=b+1
    print('b is still lower than 5 but breaks in 3')
    if b==3:
        break
if b==5:
    print('done')
elif b==3:
    print('break')

print('1-3. continue goes to the starts of the loop')
a=0
while a<5:
    a=a+1
    if not a==3:
        continue
    print('a is still lower than 5')

print('2. for loop : definite loop')
print('it will iterate on iterate variables and collection')

for i in [5,4,3,2,1]:
    print(i)
