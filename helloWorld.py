#day one python coding
import math


print(2 + 3)
print(5 - 3)
print(5 * 3)
print(700 % 200)
print(35 / 6)
print(3 ** 3)
print( 5 // 6)

your_name = "evan"
your_family_name = "aleinikovas"
your_country = "ireland"
enjoy = "im enjoying 30 days of python"

print(your_country)
print(your_family_name)
print(your_name)
print(enjoy)

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(your_country))
print(type(your_family_name))
print(type(your_name))

integer = 2
float_number = 3.0
complex_number = 4 - 4j
name = "evan"
true = True
false = False

#list ordered collection of items
my_list = [1,2,3,4,5]

#tuple data cannot be changed
tuple = (1,2,3,4,5)

#set unordered collection of unique items
my_set = {1,2,3,4,5}

# dictionary ordered collection of key-value pairs
my_dict = {'name':'evan', 'age':25}

#{\displaystyle d(p,q)=|p-q|.}
#Find an Euclidian distance between (2, 3) and (10, 8)

p = (2.3,)
q = (10.8,)

distance = math.dist(p, q)
print(distance)