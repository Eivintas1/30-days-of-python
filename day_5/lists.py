"""
lst = list()

lst = [] # Empty list can work with brackets too
# list index starts from 0

fruits = ["apple", "banana", "cherry", "date"]

print(len(fruits))

print(fruits[0])  # First item
print(fruits[1])  # Second item

rest = lst
first_fruit = fruits[0]
print(first_fruit)

#-1 is the last index of any list even if it has 99 items in it
last_fruit = fruits[-1]
print(last_fruit)

fruits.append("elderberry")

print(fruits)

vegetables = ["asparagus", "broccoli"]

all_foods = fruits + vegetables
print(all_foods)
"""
lst = list()

lst = ["hyundai","bmw","audi","mercedes","porshe"] # Empty list can work with brackets too

print(len(lst))

print(lst[0:1])
print (lst[2:3])
print (lst[4:5])

mixed_data_types = ["evan", "age: 25", "height: 6.4", "is_married: False", "address: Bj"]

it_companies = ["Google", "Meta", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))

#print first middle and last company   
first_company = it_companies[0]
middle_company = it_companies[3]
last_company = it_companies[-1]

it_companies.append("Twitter")
print(it_companies)

it_companies.insert(4, "linkedin")
print(it_companies)

#change third company to uppercase
it_companies[2] = it_companies[2].upper()
print(it_companies)

it_companies.sort()
print(it_companies)

#check if a company exists in the list
check_company = "IBM"
if check_company in it_companies:
    print(f"{check_company} exists in the list")
else:
    print(f"{check_company} does not exist in the list")
    
