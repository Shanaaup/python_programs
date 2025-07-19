n=int(input())
isprime=[True]*(n+1)
isprime[0]=isprime[1]=False
def m(i):
    for j in range(i,n+1,i):
        isprime[j]=False
for i in range(2,n+1):
    if isprime[i]:
        print(i)
        m(i)
        
    