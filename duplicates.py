n=list(map(int,input().split()))
s=set()
for i in n:
    s.add(i)
print("".join(str(i) for i in s))