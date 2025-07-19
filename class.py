class Student:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print("talk")
s1=Student('shana')
s1.talk()
print(s1.name)