# weight = 80
# height = 1.5

# bmi = int(weight) / float(height) ** 2
# bmi_as_int = int(bmi)
# print(bmi_as_int)

# print(round(8 / 3, 2))
# print(type(8 / 3))
# print(4 / 2)
# result = 4 / 2
# result /= 2
# print(result)
# score = 2
# score += 2
# print(score)
# score = 3
# print("your score is" + " " + str(score))
# score = 2
# height = 1.8
# iswinning = True
# f-string
# age_as_int = int(age)
# age = input("What is your current age?")
# age_as_int = int(age)
# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12
# message = f"You have {days_remaining}  days, {weeks_remaining} weeks,  {months_remaining}  months left."
# print(message)
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person)
# final_amount = "{:.10f}".format(bill_per_person)
# print(f"Each person should pay: ${final_amount}")
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#   print("This is an even number")
# else:
#   print("This is odd number")


# "Your BMI is 18, you are underweight."
# "Your BMI is 22, you have a normal weight."
# "Your BMI is 28, you are slightly overweight."
# "Your BMI is 33, you are obese."
# "Your BMI is 40, you are clinically obese."

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))


# bmi = round(weight / height ** 2)
# if bmi <= 18:
#   print(f"Your BMI is {bmi}, you are underweight. ")
# elif bmi <=22:
#   print(f"Your BMI is {bmi}, you have a normal weight. ")
# elif bmi <=28:
#   print(f"Your BMI is {bmi}, you are slightly overweight. ")
# elif bmi <= 33:
#   print(f"Your BMI is {bmi}, you are obese. ")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese. ")


# year = int(input("Which year do you want to check? "))


# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("leap")

#     else:
#       print("not leap")

#   else:
#     print("leap")

# else:
#   print("not leap")

# 

# # LOVE CALCULATOR
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# upper_case_name = (name1 + name2).upper()
# upper_case_name.count("name1 + name2")
# a = upper_case_name.count("T")
# b = upper_case_name.count("R")
# c = upper_case_name.count("U")
# d = upper_case_name.count("E")
# x = upper_case_name.count("L")
# y = upper_case_name.count("O")
# z = upper_case_name.count("V")
# w = upper_case_name.count("E")

# total = a + b + c +d
# total1 = x + y + z + w
# love_score = int(str(total) + str(total1))
# print(love_score)

# if (love_score < 10) or (love_score > 90):
#   print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif (love_score >= 40) and (love_score <= 50):
#   print(f"Your score is {love_score}, you are alright together.")
# else:
#   print(f"Your score is {love_score}")


# Treasure_Island

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

# x =  input("You are at a crossroad. Where do you want to go? Type \"left\" or \"right\".\n")
# if x == "left":
#   y = input("How to cross a lake,  Type \"wait\" to wait for a boat Type \"swim\" to swim across.\n")
#   if y == "wait":
#     z = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
#     if z == "red":
#       print("It's a room full of fire. Game Over.")
#     elif z == "blue":
#       print("You enter a room of beasts. Game Over.")
#     elif z == "yellow":
#       print("You found the treasure! You Win!")

  
#   else:
#    print("You get attacked by an angry trout. Game Over.")
    
# else:
#  print("You fell into a hole. Game Over.")
  
  #python list coding

# names_string = input("Give me everybody's names, separated by a comma.\n ")
# names = names_string.split(", ")

# import random
# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay + " is going to buy meal today")

# Treasure Map
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# rowindex = int(position[1]) - 1
# columnindex = int(position[0]) - 1
# map[rowindex][columnindex] = 'x'

# print(f"{row1}\n{row2}\n{row3}")

# # PLAY ROCK PAPER SCISSORS PROFESSIONALLY


# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''


# import random

# game_images = [rock, paper, scissors]
# users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
# print(game_images[users_choice])

# computer_choice = random.randint(0, 2)
# print(game_images[computer_choice])

# if computer_choice ==0 and users_choice ==1:
#   print("You Win")
# elif computer_choice == 1 and users_choice == 0:
#     print("You Loose")
# elif computer_choice == 1 and users_choice == 2:
#     print("You Win")
# elif computer_choice == 2 and users_choice == 1:
#     print("You Loose")
# elif computer_choice == 0 and users_choice == 2:
#     print("You Loose")
# elif computer_choice == 2 and users_choice == 0:
#     print("You Win")
# elif computer_choice == users_choice:
#     print("Draw")


# Height Average calculation

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

#   height_sum = 0
# count = 0

# for heights in student_heights:
#   height_sum = heights + height_sum
#   count = count + 1
#   average_height = round(height_sum/count)
# print(average_height)

# find high score

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     heighest_score = score
# print(f"The highest score in the class is: {heighest_score}")


# Sum of Even Numbers
# total = 0
# for number in range(2, 101, 2):
#    total += number
# print(total)

# FizzBuzz game

# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)

# password Generator

#     import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# password_list = []
# for letter in range(1, nr_letters +1):
#      random_letter = random.choice(letters)
#      password_list.append(random_letter) 


# for number in range(1, nr_numbers + 1):
#      random_number = random.choice(numbers)
#      password_list.append(random_number)

# for symbol in range(1, nr_symbols + 1):
#     random_symbol = random.choice(symbols)
#     password_list.append(random_symbol)
# print(password_list)
# random.shuffle(password_list)

# password=''
# for x in password_list:
#   password += ''+ x
# print(password)
# print(''.join(password_list))

# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print(number)

# x = input()
# y = x[::-1]
# if x == y:
#   print("This is palindrome")
# else:
#   print("This is not palindrome")


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
# move()
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_left()

number = 20
age = bool(number)
print(age)










