"""## **Project 1**"""

# project name : fundamental booster

#requirements :
#input(name , age, height, fav_num)
#use print()
# arithmatic op use for calculating user birth year based on age
# use formated string
# use typecasting when needed
# use id() and type() for each variable

from datetime import datetime

print(" Welcome to my fundamental booster project")
print("it is my personal interactive data collector ")

name = input("enter your name")
age = int(input("enter your age"))
height = float(input("enter your height"))
fav_num = int(input("enter your fav number \n"))
birth_year = datetime.now().year - age

print("Thank you, Here is the information we collected! \n")

print(f"name : {name} (type : {type(name)}), Memory Address {id(name)}")
print(f"age : {age} (type : {type(age)}), Memory Address {id(age)}")
print(f"height : {height} (type : {type(height)}), Memory Adress {id(height)}")
print(f"fav_num : {fav_num} (type : {type(fav_num)}), Memory Adress {id(fav_num)}")

print(f"Your Birth Year is approximately {birth_year} (based on the age of {age}) \n" )

print("Thank you for using my personal interactive data collector. I hope you have wonderful experience ")