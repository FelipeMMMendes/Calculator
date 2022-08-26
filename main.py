from __future__ import division
from art import logo

def sum(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b        

print(logo)

operations = {
    
'+':sum,
'-':subtract,
'*':multiply,
'/':division

}

num1 = float(input("Enter with a number: "))
print("""
+ - SUM
- - SUBTRACT
* - MULTIPLY
/ - DIVIDE
""")
operation = input("Enter with your operation: ")

if operation != '+' and operation != '-' and operation != '*' and operation != '/':
    print("The operation is invalid!")

calculationFunction = operations[operation]
num2 = float(input("Enter with the second number: "))

print(f"{num1} {operation} {num2} = ",calculationFunction(num1,num2))



