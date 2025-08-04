# BASIC VALUE TYPES


# string - text data represented by qoutation marks 
# string are sequences
#'This is a string' 

#NUMBERS = 
# whole numbers (int - intrergers) and Decimal Numbers (FLOAT)
#intergers like: 
#1,2,3,4
#float 
#5.1, 4.4 

#BOOLEANS : TRUE FALSE потому что тру это один а фальш это ноль по этому булеанс тоже цифры 
#_____________

#FUNCTIONS
#print - выводит инфу на эжкран 
#input - выводит инфу на экран и требует от пользователя вваести инфу - типа фидбэк появляется выделенный курсор - значит введи

#VARIABLES - boxes with value inside коробка с инфой внутри
# cтавим равно  = чтобы задачить значение

#user_name = input('Who are you? Name yourself')
#print(f'Yo, {user_name}! Wassup?')

# name it simple and common use _ (underscore)
# нельзя начинать с цифр и спец знаков
# using all uppercase only if values are constant like PASSWORD and PORT 


#CONDITIONALS - Logic blocks of code where condition is true 

#syntax: IF (condition):
#    intended block of code that will happened if condition is true (отступ в таб)
# learn more if,else,elif

#________________
#DATA STRUCTURES. structuures that help organise order 

#SEQUENCES STRUCTURES
#1 list 
#2 TUPLES
#3 SETS
#4 DICTIONARY 

#1 LISTS - ordered sequences that ordered and MUTABLE (can change inside)
# to write a list you need [] - inside are elements (str, num, booleans)
# attendents = [Pete, Walter, Maria], все в попядке им по номерам и начинается с нуля
# ID (INDEX) of list starts from 0 and stops and last number 
#SLICING - chanhe the list element inside by index

# LIST METHODS - functions that can be applied to certain type od data/structure USE SQUARE BRAKETS []
#1 APPEND (пишгется через точку и круглые скобки) adds to the end of the list 
#2 INSERT - add to the specific place in the list (POSITION INDEX, NAME OF THE ELEMENT)

#TUPLES - sequnce of elements that IMMUTABLE and ordered
# USE round brakes () 
#USEFULL FUNCTIONS for SEQUENCES
#1 LEN - длинна сиквенса или сколько элементов
#2 TYPE - какой тип 
#3 COUNT считает сколько элементов таких

#TUPLE METHODS 
#1 COUNT 
#2 INDEX 

#SETS - are unordered sequences thas dosent allow duplicates (внутри нет повторяюзихся эдементов) USE {} хорошая щштука чтобы удалить повторения 
#SET METHOD -  INTERSECTION (ищет повторения в списках)



#DICTIONARIES - complex sequence with key value pairs USE {} separete with : and , and jump a line 
#Syntax = {
# key : value,
#  key : value,
# key : value,
#  }

#ACCESING DATA OF 

#sample_dict = { 
#   "class":{ 
 #     "student":{ 
  #       "name":"Mike",
   #      "marks":{ 
    ##       "history":80
      #   }
      #}
   #}
#}
#print (sample_dict["class"]["student"]["marks"]["history"])

#LOOPS (like if, else, elif) we can run any sequence (list, tuples...RANGE)
#1 FOR LOOP 
#Syntax:
# FOR <variable> IN <sequense>;
# TAB 

fruits = ['kiwi', 'mango', 'aple', 'lime']
for fav_fruit in fruits: 

#BUILDING FUNCTION - use for LOOPS
#RANGE (start, stop, step)
# i - for iteration - типа пишут обцычно чтобы понять номер операции 
# ENUMERATE
#2 WHILE 

# ALL EXIRSISES WITH WEEK ONE 
# ПОТОМ ВИК " 1-3 "