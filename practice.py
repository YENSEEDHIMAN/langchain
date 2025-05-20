# # Simple Calculator Program in Python

# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def mul(x,y):
#     return x*y
# def div(x,y):
#     if y == 0:
#         return "Error: Division by zero"
#     return x / y

# def calculator():
#     print("select options:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     choice = int("Enter choice (1/2/3/4): ")

#     if choice not in ['1', '2', '3', '4']:
#         print("Invalid int.")
#         return
#     try:
#         num1 = float(int("Enter first number: "))
#         num2 = float(int("Enter second number: "))
#     except ValueError:
#         print("Invalid number entered.")
#         return

#     if choice == '1':
#         print("Result:", add(num1, num2))
#     elif choice == '2':
#         print("Result:", sub(num1, num2))
#     elif choice == '3':
#         print("Result:", mul(num1, num2))
#     elif choice == '4':
#         print("Result:", div(num1, num2))

# calculator()

# # Lagest of two numbers

# a= int(int("Enter the first number:" ))
# b= int(int("Enter the second number: "))
# if a>b:
#     print(f"{a} is larger than {b}")
# else:
#     print(f"{b} is larger than {a}")
    
# # Largest of three numbers

# num1 = int(int("Enter the first number: "))
# num2 = int(int("Enter the second number: "))
# num3 = int(int("Enter the third number: "))
# if num1> num2 and num1>num3:
#     print(f"{num1} is the largest number")
# elif num1 < num2 and num2 >num3:
#     print(f"{num2} is the largest number")
# else:
#     print(f"{num3} is the largest number")

# # Check number is Odd or Even
# num = int(int("Enter the number: "))
# if num %2 == 0:
#     print(f"{num} is a Even number")
# else:
#     print(f"{num} is a Odd number")

# # Multiplication of table

# num_a = int(int("Enter the number: "))
# for i in range(1,11):
#     print(f"{num_a} X {i} = {num_a * i}")

# # Factorial of a number

# num_f = int(int("Enter the number: "))
# fact = 1
# for i in range(1,num_f+1):
#     fact = fact*i
# print(fact)

# #simple intrest

# principal = int(input("Enter the principal ammount: "))
# rate = float(input("Enter the annual rate intrest: "))
# time = int(input("Enter the time: "))
# simple_intrest = (principal*rate*time)/100       #p*r*t/100
# print(simple_intrest)

# # Area of a circle
# import math
# radius_of_circle = float(input("Enter the radius of circle: "))
# area_of_circle = math.pi * radius_of_circle **2           #pi*r^2
# print(f"area of a circle is : {area_of_circle}")

# # Volume of a circle
# radius = float(input("Enter the radius of circle: "))
# volume = (4/3)*math.pi*radius**3
# print(f"volume of a circle is : {volume}")


# #Ascending Order Sort 
input_str = input("Enter numbers separated by commas: ")
numbers = [int(x.strip()) for x in input_str.split(',')]

n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Sorted list:", numbers)


#prime numbers
num = int(input("enter the number: "))
for i in range(2, num - 1): 
    if num % i == 0:
        print(f"{num} is Not prime")
        break
else:
    print(f"{num} is Prime")