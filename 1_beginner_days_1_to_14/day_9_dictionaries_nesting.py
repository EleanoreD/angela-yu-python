"""
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "key":"value, key value pairs",
}

print(programming_dictionary["Bug"])
Use the key to identify the value, when you are calling a key call it in its matching datatype, eg string or integer

adding items to the dictionary
programming_dictionary["Loop"] = "The action of doing something onver and over again."
print(programming_dictionary)

#create and empty dictionary
empty_dictionary={}

# wipe a dictionary - can reuse the variable with an empty dictionary
programming_dictionary = {}

# Edit an item in a dictionary - redefine its value
programming_dictionary["Bug"] = "A moth in your computer"
# # # print(programming_dictionary)
# #
# # #loop through a  dictionary
# # for key in programming_dictionary:

# print(key) prints the key
# print the calue use dictionary name + [key]
print (programming_dictionary[key]) prints the value

####################################################################################################
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# #TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#
#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
   score = student_scores[student]
   if score > 90:
     student_grades[student] = "Outstanding"
   elif score >= 80:
     student_grades[student] = "Exceed Expectations"
   elif score >= 70:
     student_grades[student] = "Acceptable"
   else:
     student_grades[student] = "Fail"
# 🚨 Don't change the code below 👇
print(student_grades)
#####################################################################################################################
# Nesting Lists in Dictionaries
travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
#
# def add_new_country (country_visited, times_visited, cities_visited):
#   new_country = {}
#   new_country["country"] = country_visited
#   new_country["visits"] = times_visited
#   new_country["cities"] = cities_visited
#   travel_log.append (new_country)
#
#
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
# ###############################################################################################################
# from replit import clear
# #HINT: You can call clear() to clear the output in the console.
# from art import logo
# print(logo)
#
# bids = {}
# bidding_finished = False
#
# def find_highest_bidder (bidding_record):
#   highest_bid = 0
#   winner = ""
#   #{"Angela": 123, "Sam": 341} looping through a dictioary to find the hiest value
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid:
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of £{highest_bid}!")
#
# while not bidding_finished:
#   name = input("What is your name?\n")
#   price = int(input("What is your bid? £"))
#   bids [name] = price
#   should_continue = input("Are there any other bidders? Type 'yes' or 'no'? ")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()
#
#
#     def format_name(f_name, l_name):
#       if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#       formatted_f_name = f_name.title()
#       formatted_l_name = l_name.title()
#       return f"{formatted_f_name} {formatted_l_name}"
#
#
#     # formatted_string = format_name("eleanore", "ditCHburn")
#     # print(formatted_string)
#
#     print(format_name(input("What is your first name?"), input("What is your last name?")))
# ##############################################################################################
# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formatted_f_name = f_name.title()
#   formatted_l_name = l_name.title()
#   return f"{formatted_f_name} {formatted_l_name}"
#
# # formatted_string = format_name("eleanore", "ditCHburn")
# # print(formatted_string)
#
# print(format_name(input("What is your first name?"), input("What is your last name?")))
# ####################################################################################################
# #Functions with Outputs
# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   f"Result: {formated_f_name} {formated_l_name}"
#
# #Storing output in a variable
# formatted_name = format_name(input("Your first name: "), input("Your last name: "))
# print(formatted_name)
# #or printing output directly
# print(format_name(input("What is your first name? "), input("What is your last name? ")))
#
#Already used functions with outputs.
# length = len(formatted_name)
#
# #Return as an early exit
# def format_name(f_name, l_name):
"""
"""Take a first and last name and format it
to return the title case version of the name."""
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"Result: {formated_f_name} {formated_l_name}"
# #######################################################################################
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
#
#
# def days_in_month():
#   if month > 12 or month is < 1:
#     return "invalid month"
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if is_leap(year) and month == 2:
#     return 29
#   return month_days[month - 1]
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
# ######################################################################################################
# Nesting lists and dictionaries
# {
  key: [list],
key2 :{dictionary}
}

