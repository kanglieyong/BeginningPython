class FooBar:
  def __init__(self):
    self.somevar = 42

f = FooBar()
print(f.somevar)

class FooBaz:
  def __init__(self, value=42):
    self.somvar = value

g = FooBaz("This is a constructor argument")
print(g.somvar)
