
class A:
    def sayHello(self):
        print("hello")

    def sayBye(self):
        print("bye")

class B(A):

    def sayHello(self,name):
        newstr="hello"+name
        print(newstr)

    def sayBye(self):
        print("sayonara")


bobj=B()
bobj.sayBye()
bobj.
