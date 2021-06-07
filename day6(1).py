#create a list of random number and segreagate even and odd numbers
import random
n=int(input('enter a number = '))
randomlist = random.sample(range(1,200),n)
print('your random list is :',randomlist)
odd=0
even=0
for i in randomlist:
    if i%2==0:
        even+=1
    else:
        odd+=1
        print('in list',randomlist,'even number:',even,'odd number:',odd)