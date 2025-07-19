class mammal:
    def walk(self):
        print("the animal walk")
class dog(mammal):
    pass
class cat(mammal):
    def mew(self):
        print("cat mew!!")
dog1=dog()
cat1=cat()
dog1.walk()
cat1.mew()