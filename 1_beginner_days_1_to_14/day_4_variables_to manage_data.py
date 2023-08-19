########################################################################################################################
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

#import random
#toss = #random.randint(0,1)
#if toss == 1:
  #print("You have tossed heads!")
#else:
 # print("You have tossed tails!")
#
# states_of_america = ['Delaware','New York']
# print (states_of_america [0])
########################################################################################################################
###Offset and Append Lists
# lists always start with and open variable name = [and close with]
# fruits = ["cherry", "apple", "pear"]
# print(fruits[1]) #index is the offset
# fruit = fruits[1] # we can give it a variable'
# print(fruits[-1]) #index rom the right
# fruit[1] = "banana" changes apple for banana
# fruit.append(grapes) adds an item to the end of the list
#
# Index Out of Range Error, if we try to get somethingk outside of the index.
# Whn working with a long list we often get a off by one error.  to cure this minus one to convert the
# number of items into the index.
# Nested list
# fruits = []
# vegetables = []
#
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
# [[Fruits list],[vegetables list]]
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# #Write your code below this line 👇
# import random
# player1 = int(input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
# player2 = random.randint(0,2)
# print (f"Computer chose {player2}.")
#
# if player1 >= 3 or player1 <0:
#   print("Your choice is not correct. Choose 0, 1 or 2, try again!")
# elif player1 == player2:
#   print("It's a draw!")
# elif player1 == 0 and player2 == 1:
#   print(f"Player 2 wins!\n {paper}")
# elif player1 == 1 and player2 == 0:
#   print (f"Player 1 wins!\n {paper}")
# elif player1 == 0 and player2 == 2:
#   print(f"Player 1 wins!\n {rock}")
# elif player1 == 2 and player2 == 0:
#   print (f"Player 2 wins!\n{rock}")
# elif player1 == 1 and player2 == 2:
#   print (f"Player 2 wins!\n {scissors}")
# elif player1 == 2 and player2 == 1:
#   print (f"Player 2 wins!\n {scissors}")
# else:
#   print ("Something has gone wrong, try again.")


########################################################################################################################
####BANKER ROULETTE
# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# #to find total number of items in list
# num_items = len(names)
# random_choice = random.randint(0, num_items-1)
# #print (random_choice)
# person_who_will_pay = names[random_choice]
# print (f"It is {person_who_will_pay}'s turn!'")
# # can achieve all this with random.choice(names) in the future.

########################################################################################################################
# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
#
# horizontal = int(position[0])
# vertical = int(position[0])
#
# map[vertical - 1][horizontal - 1] = "X"
#
#
# #Write your code above this row 👆
#
# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")
########################################################################################################################

########################################################################################################################

########################################################################################################################