#https://repl.it/@TobyWong/USACO-Dual-Palindromes#main.py
'''
ID: tobyewo1
LANG: PYTHON3
TASK: dualpal
'''
def readInput():
	with open("dualpal.in", "r") as f:
		imp = f.readlines()[0].strip()
		imp_lvl2 = imp.split()
		num_of_pals = imp_lvl2[0]
		lowest = imp_lvl2[1]
	return num_of_pals, lowest

def isPal(num):
	num2 = str(num)

	if num2[::-1] == num2:
		return True
	else:
		return False

def theMagic(num_of_pals, lowest):
	squares = []
	number = lowest
	while len(squares) < num_of_pals:
		squaresInNum = []
		for i in range(2, 11):
			number_as_list = []
			number_as_list.append(number)
			number_in_base = baseConversion(i, number_as_list)[0]
			if isPal(number_in_base) and number != lowest:
				squaresInNum.append(number)
		if len(squaresInNum) > 1:
			squares.append(number)
		number += 1
	return squares

		
def baseConversion(base, theList):
	theListInBase = []
	for counter in range(len(theList)):
		temp_elem = ''
		while theList[counter] != 0:
			quotient = int(theList[counter]/base)
			remainder = theList[counter]%base
			if remainder > 9:
				remainder = bases[remainder]
			theList[counter] = quotient
			temp_elem = str(remainder) + temp_elem
		theListInBase.append(temp_elem)
	return theListInBase


def writeOutput(squares):
	output = ''
	for elem in squares:
		output = output + str(elem) + "\n"
	with open("dualpal.out", "w+") as f:
		f.write(output)


num_of_pals, lowest = readInput()
num_of_pals = int(num_of_pals)
lowest = int(lowest)
# ^ works. Verified.

squares = theMagic(num_of_pals, lowest)
writeOutput(squares)
