#Reverse the words of a string
a=input("Type a sentence : ")
words= a.split()
words=list(reversed(words))
result= ' '.join(words)
print(result)