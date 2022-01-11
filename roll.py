### Dice Roll Terminal Application ###

"""
Author: Aaron C.
Start Date: 11/12/2021
Encoding: UTF-8
python 3.9

Description: Basic dice roller script intended to run from the terminal with commands. Based on ytmdl's aesthetic and functionality

This Version is tailored for Windows OS. The python package 'Colorama' is not compatable'
"""

try:
	import sys
	import random
except:
	print("ERROR: Could not import all necessary libraries.")


numDie = sys.argv[1]
typeDie = sys.argv[2]


def get_result(num, type):
	numberToRoll = num
	typeOfDie = type
	dieSet = []
    
	for i in range(0, int(numberToRoll)):
		dieSet.append(random.randint(1, int(typeOfDie)))
	print(str(dieSet))


def main(num, type):
	print("Number of Die: " + num )
	print("Type of Die: D" + type)
	get_result(num, type)


try:
	main(numDie, typeDie)
except:
	print("ERROR")