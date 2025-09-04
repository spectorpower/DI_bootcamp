# DECORATORS  arepython functions that we apply to our functions within the class i e methods 
from datetime import datetime, date #created after line 14, what is here?

class Person:

    def __init__(self, first_name, last_name, birth_date):
        self.first_name = self.format_name(first_name) #added after symbol =, after creating line 12, why?
        self.last_name = self.format_name(last_name) #added after symbol=, creating line 12, why?
        self.birth_date = self.parse_birthdate(birth_date) #added after symbol=, creating line 16, why?
    @staticmethod
    def format_name(name):
        return name.capitalize() #what name it will take?
    
    @staticmethod
    def parse_birthdate(date_str):
        return datetime.strptime(date_str, '%d-%m-%Y') #what is here ? what is mojo? and why not working

# CLASS METHOD - can be applied on class not object

    @classmethod
    def from_age(cls, first_name, last_name, age):
        current_year = datetime.today().year
        birth_year = current_year - age 
        birth_date = f'1-01-{birth_year}'
        return cls(first_name, last_name, birth_date)
    
# PROPERTY - behave like an attribute what is here
    @property
    def email(self):
        initial = self.first_name[0].lower()
        email = f'{initial}.{self.last_name.lower()}@gmail.com'
        return email #why not working  like a.stark@gmail.com

#INCAPSULATION - protected attribute  - the underscore here 
# is a convension in python - what? 
# setter ()
# getter
# deleter 
#  what are those? 

p1 = Person('john', 'snow', '21-08-1990')
print(p1.birth_date)
print(p1.first_name)
print(type(p1.birth_date))

print(datetime.now()) #for today


# how to use a class method when createing the object:

p2 = Person.from_age('aria', 'stark', 18)
print(p2.birth_date)

# DUNDER METHOTS / MAGIC METHODS 
#  __str__ 
# __repr__ 
# __eq__