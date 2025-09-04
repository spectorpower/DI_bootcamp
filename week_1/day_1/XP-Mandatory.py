
#List methods: append, remove, insert, count, clear


#exercise 1 Exercise 1: Favorite Numbers
#Key Python Topics:

#Sets
my_fav_numbers = {4, 3, 2016}
#Adding/removing items in a set
my_fav_numbers.add(42)
my_fav_numbers.add(24)
my_fav_numbers.remove(24)
friend_fav_numbers = {9, 10, 8}
#Set concatenation (using union)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers) 
print(our_fav_numbers)

#🌟 Exercise 2: Tuple
#Key Python Topics:
#Tuples (immutability)
#Instructions:

#Given a tuple of integers, try to add more integers to the tuple.
my_tuple = (1, 2, 3, 4, )
#Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
yet_another_tuple = my_tuple + (5, 6)
print(yet_another_tuple)


# 🌟 Exercise 3: List Manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana" from the list.
basket.remove('Banana')
print(basket)
#Remove "Blueberries" from the list.
basket.remove('Blueberries')
print(basket)
#Add "Kiwi" to the end of the list.
basket.append('Kiwi')
print(basket)
#Add "Apples" to the beginning of the list.
basket.insert(0,'Apples')
print(basket)
#Count how many times "Apples" appear in the list.
print(basket.count('Apples'))
#Empty the list.
basket.clear()
#Print the final state of the list.
print(basket)

#conclusion - methods are called in the following syntax:
#data-type/ data structure.METHOD_NAME()



#Recap: What is a float? What’s the difference between a float and an integer?
#Floats = basic value type for decimal numbers | INT = whole numbers
#Create a list containing the following sequence of mixed floats and integers:
#1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.

#🌟 Exercise 4: Floats
numbers = []
for i in range(8): 
    numbers.append(1.5 + i * 0.5)
print(numbers)

#Avoid hard-coding each number manually.
#Think: Can you generate this sequence using a loop or another method?



#🌟 Exercise 5: For Loop
#Key Python Topics:
#Loops (for)
#Range and indexing
#Instructions:
#Write a for loop to print all numbers from 1 to 20, inclusive.
#Write another for loop that prints every number from 1 to 20 where the index is even.



for number in range(1, 21):
    print(number)

for index, number in enumerate(range(1, 21)):
    if index % 2 == 0:
        print(number)

#exercise 6

my_name = "Nikita"  
user_input = ""

while user_input != my_name:
    user_input = input("Enter your name: ")

print("Yo,", my_name, "! You wrote it right! Move to the next exercise")