# For loop -
# fruits = ["Apple","Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "pie")
# range loop
# for number in range(1,11): # another comma adds a step
#     print(number)
#ADD all the numbers from 1 to 100
# total = 0
# for num in range(1,101):
#     total += num
# print(total)
########################################################################################################################
###EXERCISE 1 - STUDENT HEIGHTS
# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
#
# #Write your code below this row 👇
# total_height = 0
# for height in student_heights:
#   total_height += height
# print (total_height)
#
# number_of_students = 0
# for students in student_heights:
#   number_of_students +=1
# print (number_of_students)
#
# average_height =(total_height/number_of_students)
# print (average+height)
########################################################################################################################
# ### STUDENT SCORES
# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score
# print (f"The highest score is {highest_score}.")
########################################################################################################################
### Adding Evens
#Write your code below this row 👇
# total = 0
# for number in range(2, 101, 2):
#   total += number
# print (total)
########################################################################################################################
### Fizz Buzz
#Write your code below this row 👇
# for number in range (1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print ("fizz buzz")
#   elif number % 3 == 0:
#     print ("fizz")
#   elif number % 5 == 0:
#     print ("buzz")
#   else:
#     print (number)

########################################################################################################################
#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# #Eazy Level
# # password = ""
#
# # for char in range(1, nr_letters + 1):
# #   password += random.choice(letters)
#
# # for char in range(1, nr_symbols + 1):
# #   password += random.choice(symbols)
#
# # for char in range(1, nr_numbers + 1):
# #   password += random.choice(numbers)
#
# # print(password)
#
# #Hard Level
# password_list = []
#
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))
#
# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}")
########################################################################################################################