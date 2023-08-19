# Day 3 - Control Flow and Logical Operators
# Exercise 1 Odd or Even
# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print ("This is an odd number")

# print("Welcome to the roller coaster!")
# height = int(input("What is your height in cm? "))
# #Comparison Operators
# if height >= 120:
#   print ("You can ride the roller coaster!")
# else:
#   print("Sorry, you have to grow taller before you can ride.")
#########################################################################################################################
###PIZZA DELIVERY BILL
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# bill = 0
#
# if size == "S":
#     bill += 15
#
#     print("Small pizza is $15.")
# elif size == "M":
#     bill += 20
#     print("Medium pizza is $20.")
# else:
#     bill += 25
#     print("Large pizza is $25.")
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your final bill is ${bill}")

#########################################################################################################################
#
# ##BMI 2.0
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# bmi =round( weight / height ** 2)
# if bmi < 18.5:
#     print (f"Your BMI is  {bmi}, you are underweight.")
# elif bmi < 25:
#     print (f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi <30:
#     print (f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi <35:
#     print (f"Your BMI is {bmi}, you are obese.")
# else:
#     print (f"Your BMI is {bmi}, you are clinically obese.")


###Leap Year Calculator###
# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# if year % 4 == 0:
#         print("Leap year.")
# elif year % 100 == 0:
#         print ("Leap year.")
# elif year % 400 == 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")

########################################################################################################################
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# combined_string = name1 + name2
# lower_case_string = combined_string.lower()
#
# t = lower_case_string.count('t')
# r = lower_case_string.count('r')
# u = lower_case_string.count('u')
# e = lower_case_string.count('e')
# true = t+r+u+e
#
# l = lower_case_string.count('l')
# o = lower_case_string.count('o')
# v = lower_case_string.count('v')
# e = lower_case_string.count('e')
#
# love = l+o+v+e
# love_score = int(str(true) + str(love))
#
# if love_score <10 or love_score >90:
#     print (f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score >= 40 and love_score <=50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print (f"Your score is {love_score}.")
########################################################################################################################





