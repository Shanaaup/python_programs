def countzeros(n):
    result=0
    digit=1
    while True:
        posvalue,rem=divmod(n,digit)
        prefix,posvalue=divmod(posvalue,10)
        if prefix==0:
            return(result)
        if posvalue==0:
            result+=(prefix-1)*digit+rem+1
        else:
            result+=prefix*digit
        digit*=10
print(countzeros(101))