#create a list and check whether the whole list is palindrome or not
n=int(input('enter a number :'))
import random
randomlist=random.sample(range(1,200),n)
print (randomlist)
rev=randomlist[::-1]
if(randomlist == rev):
    print ('The list is a pallindrome.')
else:
    print ('The list is not a palindrome.')