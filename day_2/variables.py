#Day 2: 30 days of python programming

first_name = "Evan"
last_name = "Aleinikovas"
full_name = first_name + " " + last_name
country = "Ireland"
city = "Dublin"
age = 25
year = 2026
is_married = False
is_true = True
is_light_on = True
print("This is your ID printed out: ")
print("----------------------------------------------")
ID = first_name + " " + last_name + " " + country + " " + city
print(ID)
print("----------------------------------------------")

print(type(first_name))
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))

#compare lengths of first name and last name
if len(first_name) > len(last_name):
    print("Your first name is longer than your last name.")
elif len(first_name) < len(last_name):
    print("Your last name is longer than your first name.")
else:
    print("Your first name and last name are of equal length.")

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_div = num_one // num_two

#radius of a circle
radius = 30
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius

input_radius = int(input("Enter radius: "))
area = 3.14 * input_radius ** 2

input_name = input("Enter your name: ")
print("Hello " + input_name)
input_age = int(input("Enter your age: "))
print("You are " + str(input_age) + " years old.")
input_country = input("Enter your country: ")
print("You live in " + input_country)