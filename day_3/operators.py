
age = 18
height = 1.94
complex_num = 2 + 3j



input_base = int(input("Enter base: "))
input_height = int(input("Enter height: "))
area_of_triangle = 0.5 * input_base * input_height
print("The area of the triangle is: " + str(area_of_triangle))

input_a = int(input("Enter side a: "))
input_b = int(input("Enter side b: "))
input_c = int(input("Enter side c: "))
perimeter_of_triangle = input_a + input_b + input_c
print("The perimiter of the trangle is: " + str(perimeter_of_triangle))

prompt = "Enter length: "
length = int(input(prompt))
width = int(input("Enter width: "))
area_of_rectangle = length * width
print("The area of the rectangle is: " + str(area_of_rectangle))
perimeter_of_rectangle = 2 * (length + width)
print("The perimeter of the rectangle is: " + str(perimeter_of_rectangle))

prompt_circle = "Enter radius: "
radius = int(input(prompt_circle))
pi = 3.14
area_of_circle = pi * radius ** 2
print("The area of the circle is: " + str(area_of_circle))
circum_of_circle = 2 * pi * radius
print("The circumference of the circle is: " + str(circum_of_circle))

calculate_slope = "y = 2x -2"
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
print("The slope is: " + str(slope))

hours_worked = int(input("Enter hours worked: "))
rate_per_hour = int(input("Enter rate per hour: "))
weekly_earnings = hours_worked * rate_per_hour
print("Your weekly earnings are: " + str(weekly_earnings))

number_of_years_lived = int(input("Enter number of years you have lived: "))
seconds_in_a_year = 365 * 24 * 60 * 60
total_seconds_lived = number_of_years_lived * seconds_in_a_year
print("You have lived for " + str(total_seconds_lived) + " seconds.")

#script 

for i in range(1,6):
    print(f"{i}\t{i**1}\t{i**2}\t{i**3}\t{i**4}\t{i**5}")