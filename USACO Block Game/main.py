#http://www.usaco.org/index.php?page=viewproblem2&cpid=664
'''
ID: tobyewo1
LANG: PYTHON3
TASK: blocks
'''
def readInput():
	with open("blocks.in", "r") as f:
		raw = f.readlines()
		numblocks = int(raw[0].strip())
		blocks = []
		for i in range(numblocks):
			blocks.append(raw[i+1].strip())
	return blocks

def countlettersinword(blocks):
	letters = {}
	alphabet = []
	for i in range(97, 123):
		letters[chr(i)] = 0
		alphabet.append(chr(i))
	for elem in blocks:
		side1 = elem.split()[0]
		side2 = elem.split()[1]
		side1dict = {}
		side2dict = {}
		for elem in side1:
			if elem in side1dict:
				side1dict[elem] += 1
			else:
				side1dict[elem] = 1
			if elem not in side2dict:
				side2dict[elem] = 0
		for elem in side2:
			if elem in side2dict:
				side2dict[elem] += 1
			else:
				side2dict[elem] = 1
			if elem not in side1dict:
				side1dict[elem] = 0


		for letter in side1dict.keys():
			if side1dict[letter] >= side2dict[letter]:
				letters[letter] += side1dict[letter]
			elif side2dict[letter] > side1dict[letter]:
				letters[letter] += side2dict[letter]
	return letters


def output(letters):
	output = ''
	with open("blocks.out", "w+") as f:
		for elem in letters:
			output += str(letters[elem]) + "\n"
		f.write(output)


blocks = readInput()
letters = countlettersinword(blocks)
output(letters)


#homework:
#http://www.usaco.org/index.php?page=viewproblem2&cpid=665


#if you finish early:
#http://www.usaco.org/index.php?page=viewproblem2&cpid=687
