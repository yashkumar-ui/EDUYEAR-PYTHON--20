#reverse the words of a string
wrd=input('Type a sentence :')
wrd=wrd.split()
wrd=list(reversed(wrd))
print(' '.join(wrd))