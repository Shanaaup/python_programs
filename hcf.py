n=list(map(int,input().split()))
a=n[0]
b=n[1]
for i in range(1,len(n)-1):
#a=int(input())
#b=int(input())
    while a%b!=0:
        b,a=a%b,b
        k=b
    a=max(b,n[i])
    b=min(b,n[i])
print(k)