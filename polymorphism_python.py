a=20
b=30
print(a+b)
print("hello"+"python")
l=[1,2,3,4]
t=(1,2,3,4,5)
print(len(l))
print(len(t))
class animal:
    def age(self):
        print("from animal age")
        def color(self):
            print("from animal color")
class rabbit(animal):
    def age(self):
        print("from rabbit age")
        def color(self):
            print("from rabbit color")
class bear(animal):
    def age(self):
        print("from bear age")
        def color(self):
            print("from bear color")
a_obj=animal()
r_obj=rabbit()
b_obi=bear()
# for object in(a_obj,r_obj,b_obj):
# object.color()
# object.age()

class Purchase:
    def __int__(self,order_items_buyer):
      self.order_items=list(order_items)
      self.buyer=buyer
    def __len__(self):
      return len(self.order_items)
    def __repr__(self):
      return "my purchase objects is{}".format(self.buyer)
# Purchase_obj=Purchase(['fruits','electronics','food'],buyer = "madhu")
# print(len(Purchase_obj))
# print(Purchase_obj)
class A:
    x=100
    def method_a(self):
        print("from class A")
class B(A):
    def method_b(self):
        print("from class B")
        print(super().x)
        super().method_a()
obj=B()
obj.method_b()
class A:
    def method(self):
        print("from class A")
class B(A):
    pass
b=B()
b.method()
a=10
a=200
print(a)
def print_name():
  return "hello"+"madhu"
def print_name(name):
  return "hello"+"{}".format(name)
print(print_name("python"))




