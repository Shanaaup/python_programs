secret_no=8
limit=0
while limit<4:
    limit+=1
    guess=int(input("enter the guess:"))
    if guess==secret_no:
        print("you won!!!!")
        break
    else:
        print("you are wrong")
    


