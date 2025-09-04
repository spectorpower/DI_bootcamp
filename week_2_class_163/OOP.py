# OOP 

# CLASS = a blueprint of the object , where we will define what are properities and behaviors of the object

# SYNTAX

class Dog: # must have propirietes or behavior or both 
    def __init__(self, breed, nickname, color, age, is_trained = False):  # self first the constructor function for PROPERITIES
        print('object was created')     #what is here?
        self.breed = breed #key and value 
        self.nickname = nickname
        self.color = color
        self.age = age 
        self.is_trained = is_trained
        self.dogs_years_age = age * 7 # added later 
# self is the internal dictionary that has the properities from the class 
# self is dictionary {breed:..., nickname:..., color:....} #what is self anyway?

# creating an object from the class dog:
dog1 = Dog('chowchow', 'lion', 'orange', 5)
dog2 = Dog ('collie', 'lady', 'bege and white', 15, True)
dog2.is_servise_dog = True #creating spesific attribute to a specific dog object 

print(dog1.color) # we can get accessof the attribute if we use DOT NOTATION
print(dog1.__dict__)  #what is here?
print(dog2.__dict__)  #what is here?

#1 create a new attribute to the Dog class called "is_trained" the value 
# is a boolean and the default is False  
# that were created before this new attribute was added?

#########################

# INSTANCE METHODS
# is a function that linked to a class
# MEthod is the behavior of an object
# every function is a method but not the other way 


class Dog: 
    def __init__(self, breed, nickname, color, age, is_trained = False):  
        print('object was created')     
        self.breed = breed 
        self.nickname = nickname
        self.color = color
        self.age = age 
        self.is_trained = is_trained

    def bark(self):
        print(f'{self.nickname} is barking') #what is here?
print(dog1.color) 
print(dog1.__dict__) 
print(dog2.__dict__) 

dog3 = Dog('labrador', 'Rex', 'gold', 7, True)
dog3.bark() # calling the method of object #what is here?
Dog.bark(dog3) #another way of calling the method of object but# what is here?

def sit(self): # why self again? #what is here?
        if self.is_trained == True:
            print(f'{self.nickname} is not trained') #not working and why and #what is here?
