class a():
    def fun(self):
        print("A")
class b():
    def fun(self):
        print("B")
class c(b,a):
    def funn(self):
        print("c")

obj = c()
obj.fun()