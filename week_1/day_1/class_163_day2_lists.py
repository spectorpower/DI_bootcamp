#sequence - all today are sequences 
# list is a mutubale (can be changed) sequence of elements 
# we must use square brackets []
# each element got the Index - ID []

my_list = [ 'Hatty', 'Ron', "Hermione"] # here it will print elemnt by element 
my_list2 = list('Harry') #

# Index: a position number on the sequence and it starts from 0 with the end position +1

# list methods 
fruits = ['apple', 'mango', 'kiwi', 'lime']
# we want to add another element without hardcode
fruits.append('banana') #adds element to the last index of the list
# if we want to add element to some position
fruits.insert(1,'watermelon') #first is index then the element, insert the shift all position
# if we need to remove sertain element
fruits.remove('mango') #one element at the time and the first apperiance 
# deleting the last position element
fruits.pop() #empty
# deleting exact index 
fruits.pop(2)  


# TUPLE : immutable and ordered (cant be changed)
#  use (), must be at least two elements

numbers = (10,20,30,40,50,20)
number2 = tuple(numbers)
print(number2)

numbers.count(20) # will count how many times 20 in the tuple
numbers.index(20)

#concatinate tuples
fruits = ('apple', 'mango', 'kiwi', 'lime')
vegs = ('tomato', 'potato', 'lettuce')
fruits_vegs = fruits + vegs 
print (fruits_vegs)

a,b,c,d,e,f = numbers 
print(a)
print(b)
print(c)
print(d)

# SETS = unordered sequence without duplicated elements and using {}

my_set = {1,4,8,9}
my_set2 = set(my_set)
# if we need to ad number
my_set.add(55)

#  SET METHODS
names= {'Juliana', 'Israel', "Dina"}
countries = {'USA', 'Brasil', 'Israel'}
names.intersection(countries)
names.difference(countries)
countries.difference(names)

my_fav_colors = {'black', 'white', 'purple'}
my_fav_colors.add('grey')
print(my_fav_colors)
friend_fav_colors = {'orange', 'green', "white"}
my_fav_colors.intersection(friend_fav_colors)
print(my_fav_colors.intersection(friend_fav_colors))
my_fav_colors.clear()

# LOOPS 
# very fundamental in coding in every language, loops can reach element
# and it called Iteration (each loop)
# we have FOR LOOPS and WHILE LOOPS

#  FOR <variable> IN <sequence/iterable>:
    # intendet block that will happened in each iteration

# what we can loop?
# strings
# lists
# tuples
# sets
# range     

for char in 'student': #here we createn new variable char
    print(char) 
# Looping through a list structure
fruits = ['apple', 'watermelon', 'banana']
for each_fruit in fruits:
    print(f'I do love {each_fruit}')

# looping in sequence, i is integer 
for i in range(1,11,2): #started from 1 and stop 10, with step 2
    print(i)
for i in range(1,11,): #or without step - 1 is by default
    print(i)

for i in range(len('student')):
    print(i)