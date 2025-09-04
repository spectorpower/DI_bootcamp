# Functions
# SYNTAX 
# def <name>():
# intended block of code
# returned value

# def say_hello():
#     print('Hello, I am a function output')
# say_hello() # calling the function


# DOC STRINGS: documentation for the function
# def say_hello(language:str):
#     '''prints a greeting depending on the language argument'''
#     if language == 'PT':
#         print('Oi, eu sou uma funcao')

#     elif language == 'HE':
#         print('Типа это иврит')
    
#     else:
#         print('Hello, i am a function')

# say_hello('HE')


# positional argument : we pass only the value
# keyword arguments : we explicity define to wich arguments the value is related 

# mixinf positional and keyword argument: we can mix but every  positional arguments needs to be first

# return keyword: it returns  a value from the function RETURN

# SCOPE 
# Local scope : inside (intented after the function def) the function
# we only can access the variable on the local scope of a function if we use the RETURN keyword
#  to connect function we can use keyword GLOBAL (we cant access a local variable on global scope)
# GLOBAL SCOPE : not in the scope of a function (its in the main file)


# DATA STRUCTURES: lists, tuples, sets, and ductionaries
# HOW TO WORK WITH THEM ON FUNCTION

students = ['Harry', 'Hermione', 'Ron', 'Luna']

def welcome():
    for name in students:
        print(f'{name}, Welcome to Hogwarts!')

welcome()

def get_house():
    for i, name in enumerate(students):
        students[i] = f'{name} - Griffyndor'

    if name == 'Luna':
        students

get_house()
print(students)
students[0] = f'{students[0]} - Griffyndor'

