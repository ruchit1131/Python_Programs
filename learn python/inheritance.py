class Parent(object):

    def override(self):
        print("Parent")

class Child(Parent):

    def override(self):
        print("Child")

    def test(self):
        Parent.override(self)

dad=Parent()
son=Child()
dad.override()
son.override()
son.test()
