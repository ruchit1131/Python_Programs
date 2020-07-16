#using super() with __init__
class Parent(object):
    def __init__(self):
        print("Parent")

class Child(Parent):
    def __init__(self,stuff):
        self.stuff=stuff
        print(stuff,"before")
        super(Child,self).__init__()
        print(stuff,"after")


son=Child("kk")
help(son)
#if no constructor in defined in the base class then the parent class constructor is inherited
#else constructor in not inherited and has to be explicitely called using super
