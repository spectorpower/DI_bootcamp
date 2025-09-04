# OOP INHERITANCE  - 

class Animal: #parent class

    def __init__(self, name, family, legs):
        self.name = name
        self.family = family
        self.legs = legs 
    def sleep(self):
        print(f'{self.name} is sleeping (parent class)')

class Dog(Animal): #child class
# super(). waht is that? 

   def sleep (self):
       print(f'{self.name} is sleeping (child class)') #What is here?
def fetch_ball(self):
       print(f'{self.name} is running for the ball')
       
dog1 = Dog('Rex', 'Canin', 4)
print(dog1.legs)
dog1.sleep()

class Cat(Animal):
    def sleep(self):
        base_msg = super().sleep()
        print(f'{base_msg} is sleeping')

# super(). what is that? 
# you can get access to inheritance 
# what is multiple inheritance 
#  what is "except" in "try" and how its different from "else"?
#  what is "finally"


class Animal: #parent class

    def __init__(self, name, family, legs):
        self.name = name
        self.family = family
        self.legs = legs 
    def sleep(self):
        print(f'{self.name} is sleeping (parent class)')
