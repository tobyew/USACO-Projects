#https://repl.it/@TobyWong/USACO-Palindromic-Squares#main.py
'''
ID: tobyewo1
LANG: PYTHON3
TASK: palsquare
'''

bases = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "I", 19:"J", 20:"K"}
#https://mathbits.com/MathBits/CompSci/Introduction/frombase10.htm


def readInput():
	with open("palsquare.in", "r") as f:
		return int(f.readlines()[0].strip())
def getSquares():
	squares = []
	regular = []
	for n in range(1, 301):
		regular.append(n)
		squares.append(n*n)
	return squares, regular
def baseConversion(base, squares):
	squaresInBase = []
	for counter in range(len(squares)):
		temp_elem = ''
		while squares[counter] != 0:
			quotient = int(squares[counter]/base)
			remainder = squares[counter]%base
			if remainder > 9:
				remainder = bases[remainder]
			squares[counter] = quotient
			temp_elem = str(remainder) + temp_elem
		squaresInBase.append(temp_elem)
	return squaresInBase

def checkIfPal(regularsInBase, squaresInBase):
	output = []
	counter = 0
	for elem in squaresInBase:
		if elem[::-1] == elem:
			output.append([regularsInBase[counter],elem])
		counter += 1
	return output

def writeOutput(pals):
	output = ""
	for elem in pals:
		output += str(elem[0]) + " " + str(elem[1]) + "\n"
	with open("palsquare.out", "w+") as f:
		f.write(output)
		

		

base = readInput()
squares, regular = getSquares()
squaresInBase = baseConversion(base, squares)
regularsInBase = baseConversion(base, regular)
pals = checkIfPal(regularsInBase, squaresInBase)
writeOutput(pals)
#note: we have to go through the squares twice, maybe we could only go through them once if i just convert base as we get the square


#homework: do-el palindromes question, copy some functions

