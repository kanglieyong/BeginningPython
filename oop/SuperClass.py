class A:
  def hello(self):
    print("Hello, I'm A")

class B(A):
  pass

class C(A):
  def hello(self):
    print("Hello, I'm C")

a = A()
b = B()
c = C()

a.hello()
b.hello()
c.hello()

