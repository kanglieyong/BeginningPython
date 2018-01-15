class Bird:
  def __init__(self):
    self.hungry = True
  def eat(self):
    if self.hungry:
      print("Aaahh...")
      self.hungry = False
    else:
      print("No, thanks")

class SongBird(Bird):
  def __init__(self):
    super(SongBird, self).__init__()
    self.sound = "Squawk!"
  def sing(self):
    print(self.sound)

b = Bird()
b.eat()

sb = SongBird()
sb.sing()
sb.eat()
