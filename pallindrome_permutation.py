from collections import Counter
n=input()
#in pallindrome atmost one charachter has odd count.
c=Counter(n)
oddchar=0
for i in c.values():
    if i%2==1:
        oddchar+=1
        
if oddchar>1:
    print("False")
else:
    print("True")