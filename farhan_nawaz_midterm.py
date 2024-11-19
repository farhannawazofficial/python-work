# Farhan Nawaz
# Gmail (farhannawaz@gmai.com)
# Number (03480278285)
# ID Number (22569)

# ------------------------------------------Question Number 1--------------------------------------------------------
# Write a Python program to do arithmetical operations addition and division.

# #Anwsar 01 (part 01 - sum/additions)
num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))
sum = num1 + num2
print("sum:", num1, "+", num2, "=", sum)

# part 02 - Deivision
dividend = float(input("Enter the dividend for division: "))
divisor = float(input("Enter the divisor for division: "))
division = dividend / divisor
print("Division:", dividend, "/", divisor, "=", division)

# part 02 - Number of power sum
number = int(input("Enter Number: "))
power = int(input("Enter Power: "))
result = number ** power
print(f"Result: { number} ^ {power} = {result}")

# part 02 - Number of power divident
dividend = int(input("Enter Divident: "))
divisor = int(input("Enter Divider: "))
result = dividend // divisor
print(f"Result: {dividend} // {divisor} = {result}")

#---------------------------------------------Question 01 Completed-------------------------------------------

#---------------------------------------------Question Number 02-------------------------------------------------
# Write a Python program to find the area of a triangle.

# Answar 02
# Get the base and height of the triangle from the user
base = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area using the formula area = (base * height) / 2
area = (base * height) / 2

# Print the calculated area
print("The area of the triangle is:", area)

# ---------------------------------------------Question Number 02 completed ----------------------------------------------

#---------------------------------------------Question Number 03-------------------------------------------------
#Write a Python program to convert Celsius to Fahrenheit.

#Answar 03
# Get the temperature in Celsius from the user
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit using the formula
fahrenheit = (celsius * 9/5) + 32
# Print the result in the specified format
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")

#----------------------------------------------------Question Number 03 completed ------------------------------------------

#---------------------------------------------Question Number 04-------------------------------------------------
#Write a Python program that return all datatypes that we discussed in the class.

#Answar 04
# Integer
number = 19
print("The Data Type of", number, "is", type(number))

# Float
decimal_number = 16.5
print("The Data Type of", decimal_number, "is", type(decimal_number))

# String
name = "Farhan Nawaz"
print("The Data Type of", name, "is", type(name))

# Boolean
boolean_value = True
print("The Data Type of", boolean_value, "is", type(boolean_value))

# List
list_of_numbers = [1, 2, 3]
print("The Data Type of", list_of_numbers, "is", type(list_of_numbers))

# Tuple
tuple_of_numbers = (4, 5, 6)
print("The Data Type of", tuple_of_numbers, "is", type(tuple_of_numbers))

# Set
set_of_numbers = {7, 8, 9}
print("The Data Type of", set_of_numbers, "is", type(set_of_numbers))

#----------------------------------------------------Question Number 04 completed ------------------------------------------


