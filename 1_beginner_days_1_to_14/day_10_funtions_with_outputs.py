# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formatted_f_name = f_name.title()
#   formatted_l_name = l_name.title()
#   return f"{formatted_f_name} {formatted_l_name}" # we have told it what to return here
#
# # formatted_string = format_name("eleanore", "ditCHburn")
# # print(formatted_string)
#
# print(format_name(input("What is your first name?"), input("What is your last name?")))
# # #########################################################################################
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
# #         return False
# #     else:
# #       return True
# #   else:
# #     return False
# #
# # def days_in_month():
# #   if month > 12 or < 1:
# #     return "Invalid month"
# #
# #   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# #   if is_leap(year) and month == 2: # the True or False flag makes this work
# #     return 29
# #   return month_days[month-1]
# #
# # # 🚨 Do NOT change any of the code below
# # year = int(input("Enter a year: "))
# # month = int(input("Enter a month: "))
# # days = days_in_month(year, month)
# # print(days)
# ############################################################################################
# #  Doc Strings
# # Small bits of documentation as we code.
# def format_name(f_name, l_name):
#   """This is the docstring, take a first and last name and formati it
#   to return the title case of the name."""
#   # then rest of function here. It adds the comment above and adds it into the aut explain on hover
# #############################################################################################
# # ## CALCULATOR
#Calculator
# def add(n1, n2):
#   return n1 + n2
#
# def subtract(n1, n2):
#   return n1 - n2
#
# def multiply(n1, n2):
#   return n1 * n2
#
# def divide(n1, n2):
#   return n1 / n2
#
# operations = {
#   "+": add,
#   "-": subtract,
#   "*": multiply,
#   "/": divide
# }
#
# num1 = int(input("What's the first number?: "))
# for symbol in operations:
#   print(symbol)
#
# #Here we select "+"
# operation_symbol = input("Pick an operation: ")
# num2 = int(input("What's the next number?: "))
# calculation_function = operations[operation_symbol]
# first_answer = calculation_function(num1, num2)
#
# print(f"{num1} {operation_symbol} {num2} = {first_answer}")
#
# #Here we select "*" which overides the "+" we selected on line 26.
# operation_symbol = input("Pick an operation: ")
# num3 = int(input("What's the next number?: "))
#
# #Here the calculation_function selected will be the multiply() function
# calculation_function = operations[operation_symbol]
#
# #Here the code will be:
# #second_answer = multiply(multiply(num1, num2), num3)
# second_answer = calculation_function(calculation_function(num1, num2), num3)
# #second_answer = 2 * 3 * 3 = 18
# #To fix this bug we need to change the code on line 42 to:
# second_answer = calculation_function(first_answer, num3)
# #In the next lesson, we will delete all the code from line 34-48 so don't worry
# #It won't affect your final project.
# #But it's a good oportunity to practice debugging. 🐞
#
# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

######################################################################################################################
### PRINT V RETURN
""" with retunr we can use the vause for futher calculations and uses."""
### CALCULATOR FINAL CODE
from replit import clear
from art import logo


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

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()


calculator()
#####################################################################################################################

