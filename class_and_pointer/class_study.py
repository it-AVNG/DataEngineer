class Cookie:
    def __init__(self,color):
        self.color = color
    
    def get_color(self):
          return self.color

    def set_color(self, color):
         self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')


print("the color of cookie one is:", cookie_one.get_color())
print("the color of cookie two is:", cookie_two.get_color())

cookie_two.set_color('yellow')

print("the color of cookie two is:", cookie_two.get_color())