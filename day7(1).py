#give all the index values of vowels
#clean bug
ori=input('Write a sentence :')
a=[]
for i in range (len(ori)):
   if ori[i] in 'aeiou':
        a.append(i)
        print('The vowel indices are:', a)