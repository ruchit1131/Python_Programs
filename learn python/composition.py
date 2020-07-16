from Aclass import Other

class Child(object):

    def __init__(self):
        self.Other=Other()#By composition, in our classes under development, we explicitly declare data members as objects of some existing classes.

    def implicit(self):
        Other.implicit(self)# or self.Other.implicit(self)

    def override(self):
        print("Child Override")

    def altered(self):
        print("Child before altered")
        Other.altered(self)
        print("Child after altered")

son=Child()
son.implicit()
son.override()
son.altered()

#We can write the Other class in this file as well. And we can import it from other module as well
