import collections
x=raw_input('Enter the location of the text file')
f = open(x,'r')
a = f.read()
print(a)
f.close()
gram=[]
arithm=[]
pososto=[]
le=collections.Counter(a).most_common()
sorted(le, key=lambda tup: tup[1])
for i in range(len(le)):
    if (le[i][0])!=" ":
        gram.append(le[i][0])
        arithm.append(le[i][1])
        
pososto=[]
for i in range(len(gram)):
    pososto.append(arithm[i]/sum(arithm))
    print('THE LETTER '+gram[i]+'  APPEARS',arithm[i], 'TIMES')  
    







most= collections.Counter(a).most_common()[0]
less= collections.Counter(a).most_common()[-1]
if " "==less[0]:
    less=collections.Counter(a).most_common()[-2]
if " "==most[0]:
    most=collections.Counter(a).most_common()[1]



print(most[0])
print(less[0])

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


m=findOccurrences(a, most[0])

l=findOccurrences(a, less[0])
for i in range(len(m)):
    a=a[:m[i]]+less[0]+a[m[i]+1:]
for i in range(len(l)):
    a=a[:l[i]]+most[0]+a[l[i]+1:]
print a.upper()






  #  for i in range(len(a1)):
  #      if a1[i]==a2[s1]:
  #          a1[i]=a2[s2]
  #      elif a1[i]==a2[s2]:
 #           a1[i]=a2[s1]
 #   print ("".join(a1)),


#makari('patata')   
#f = open('test.txt','r')
#x = f.read()
#f.close()
#import re
#y = re.split("(\s+)",x)

#for i in range(len(y)):
#    if " " not in y[i]:
#        makari(y[i])
#    else:
#        print(y[i]),



















