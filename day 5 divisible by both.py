# from range n=m , print all the number divisible by 5 and 7 both
n= int(input('enter range starting no. = '))
m= int(input('enter range last no. = '))

for x in range(n,m+1):
    if x%5==0 and x%7==0:
        print(x,'is divisible by 5 and 7')