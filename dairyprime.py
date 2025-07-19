
def isprime(m):
    for  i in range(2,m//2):
        if m%i==0:
            return False
    return True
n=int(input())

for i in range(n):
    if isprime(2,i):
        print(i)
        