### Day 2 Data Types
#Exercise 1
# len will only run with a string
# String is a string of characters
# Int is an integer whole number
#Float
#Print("Hello"[0]) printing out the index of a string
# Boolean True or False only


# num_char = len(input("What is your name? \n"))
#
# #type(num_char)
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# a = 123
# print(type(a))

#a = float(123)
#print(type(a))

# Exercise 1
# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆
#
# ####################################
# #Write your code below this line 👇
# first_digit = two_digit_number [0]
# second_digit = two_digit_number [1]
# print (int(first_digit)+int(second_digit))

# Exercise 2 - BMI Calculator
# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# bmi = int(weight) / float(height)**2
# bmi_as_integer = int(bmi)
# print (bmi_as_integer)

# Exercise 3 - Life in Weeks
# 🚨 Don't change the code below 👇
#age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# age_as_int = int(age)
#
# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12
#
# message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
#
# print(message)

# To round a number up or down
#print(round(8/3, 3)) # with rounding to three decimal places
# print(8//3) # floor division to produce an integer rather than a floating point number.

# Exercise 2 BMI Calculator
# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
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

# Exercise 3
# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# if year % 4 == 0:
#         print("Leap year.")
# elif year % 100 == 0:
#         print ("Leap year.")
# elif year % 400 == 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")

# += adds 1 to the value -= removes 1 f
########################################################################################################################
