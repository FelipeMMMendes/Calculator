from __future__ import division
from art import logo

def sum(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b        

print(logo)

operations = {
    
'+':sum,
'-':subtraction,
'*':multiplication,
'/':division

}

def calculator():
    num1 = float(input("Enter with a number: "))
    print("""
    + - SUM
    - - SUBTRACT
    * - MULTIPLY
    / - division
    """)
    operation = input("Enter with your operation: ")

    if operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print("The operation is invalid!")

    calculationFunction = operations[operation]
    num2 = float(input("Enter with the second number: "))
    answer = calculationFunction(num1,num2)

    print(f"{num1} {operation} {num2} = ",answer)

    #Variavel flag para controlar a repeticao da calculadora
    ContinueOperations = True

    while ContinueOperations:

        CalculatorContinue = input(f"Do you want to execute another operation with the number {answer}? (Y/N): ")

        if CalculatorContinue=='Y':
            operation = input("Enter with your operation: ")
            calculationFunction = operations[operation]
            
            if operation != '+' and operation != '-' and operation != '*' and operation != '/':
                print("The operation is invalid!")

            num1 = answer
            num2 = float(input("Enter with the second number: "))

            answer = calculationFunction(num1,num2)

            print(f"{num1} {operation} {num2} = ",answer)
        else:
            ContinueOperations = False    
    

    



