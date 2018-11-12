from pythonlangutil.overload import Overload, signature


class A:

    @Overload
    @signature()
    def  my_print_method(self):
        print("My print method")

    @my_print_method.overload
    @signature("int")
    def my_print_method(self, i):
        print('second method', i)

    @my_print_method.overload
    @signature("str")
    def my_print_method(self,my_string):
        print('second method',my_string)

aobj = A()

aobj.my_print_method()
aobj.my_print_method(7)
aobj.my_print_method("Hello")