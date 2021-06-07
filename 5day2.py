#find sum of series 2+22+222+2222+.....
print('printing sum of givien terms of series 2 + 22 + 222 + 2222 + ...n\n ')
a=int(input('enter number of terms = '))
term = 2
sums =0
for i in range (1,a+1):
    sums =sums+ term
    print(term)
    term=2+term*10