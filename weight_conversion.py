weight=int(input("enter the weight without unit:"))
unit=input("choose(k for killograms and p for pounds): ")
if unit.lower()=='k':
    convert=weight*2.2046
    print("weight in pounds:"+str(round(convert,2)))
elif unit.lower()=='p':
    convert=weight/2.2046
    print("weight in killogram:"+str(round(convert,2)))
else:
    print("invalid unit")