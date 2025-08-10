#description = 'strings are...' 
#print (description.upper())
#print (description.replace("are", "is"))
#print (description.split()[0])
#my_age = 40
#print (('dude, you gonna be'),my_age + 123879)

bank_balance = "33000"
phone_number = 532287514
print (type (bank_balance))
print (type(phone_number))
bank_balance = int(bank_balance)
phone_number = str(phone_number)
print (type (bank_balance))
print (type(phone_number))

my_name = 'Nikita'
my_mishpaha = 'Spector'
print('yo', my_name, my_mishpaha)

name = "Alice"
age = 30
city = "New York"
print (f'Yo {name}!You are {age} years old and you do live in {city}')

x = 5  
y = 10  
z = 0  
word1 = "hello"  
word2 = "world"
if x < y:
    print('cool')
if y > z:
    print('Ya man')
if word1 != word2:
    print('hell yeah!')
if x < y > z:
    print('just uotstanding')

print(bool(word1))
print(bool(z))

movie = "The Matrix"
year = 1999
main_actor = "Keanu Reeves"
rating = 8.7
print(f'🎬 {movie} released in {year} starring {main_actor} has a rating of {rating} score')


#age = input('How wise are you, dude?')
#age = int(age)
#years_until_100 = 100 - age 
#print(f'Well, in {years_until_100} years you gonna turn 100 years wise')

#name = input ("what's your name, braveheart?")
#if len(name) <= 5:
#    print('you got pretty short name')
#if len(name) >8:
#    print('are you like Slartibartfast or something?')
#else:
#    print('pretty common')

#number = int(input('Give me a number'))
#if number %3 == 0 and number %5==0:
#    print('Fine, this number is devisible by 3')
#else:
#    print('good, but can you devide it by 3 and 5?')

#sentence = "I'am learning Python programming!"
#word = input('Now enter a word for serch')
#if word in sentence:
#    print (f'Fine, there is such a word in {sentence}')
#else:
#    print (f'Nope, can\'t see such thing in {sentence}')

#number = int(input('So give me any number from 1 to 100:'))
#if not 1 <= number <= 100:
#    print ('i told you to give number from 1 to 100')
#if  number %3 == 0 and number %5 == 0:
#    print ('FizzBuzz')
#elif number %3==0:
#    print ('Fizz')
#elif number %5==0:
#    print('Buzz')
#else:
#    print('wrong - do it again')



#sample_dict = {
#  "name": "Kelly",
#  "age": 25,
#  "salary": 8000,
#  "city": "New york"
#}
#keys_to_remove = ["name", "salary"]
#for keys in keys_to_remove:
#    del sample_dict[keys]
#print(sample_dict)

