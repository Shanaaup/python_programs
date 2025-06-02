command=""
while command!='quit':
    command=input(">").lower()
    if command=='start':
        print("car starts")
    elif command=='stop':
        print("the car stops")
    elif command=='help':
        print(''' 
              start-start car
              stop-car stop
              quit-end the game''')
    elif command=='quit':
        break
    else:
        print("i don't understand")