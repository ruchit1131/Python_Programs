class Parent(object):
    def altered(self):
        print("Parent\n\n")
    def abc(self):
        print("Function abc()")

class Child(Parent):

    def altered(self):
        print("Child before")
        super(Child,self).altered()
        print("Child after")
        Parent.altered(self)


dad=Parent()
son=Child()

dad.altered()
son.altered()
dad.abc()
son.abc()

