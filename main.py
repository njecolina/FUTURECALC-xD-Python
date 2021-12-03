from os import system, name

from art import logo

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    q = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or 'x' for exit: ")

    if q == 'y':
      num1 = answer
    elif q == 'n':
      should_continue = False
      clear()
      calculator()
    else:
      should_continue = False
      clear()
      print("Thank you for using FUTURECALC :)")

calculator()
