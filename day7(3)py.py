#remove duplicate elements without using set
#remove bug
list=[1,2,2,3,4,5,4,3,4,5]
print(list)
new=[]
for i in list:
    if i not in new:
        new.append(i)
        print("New list without repeated element is :",new)