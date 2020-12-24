#https://train.usaco.org/usacoprob2?a=fxKXvyWsW9y&S=crypt1
'''
ID: tobyewo1
LANG: PYTHON3
TASK: crypt1
'''

def readInput():
	with open("crypt1.in", "r") as f:
		raw = f.readlines()
	nums = []
	for i in range(0, int(raw[0].strip())*2, 2):
		nums.append(int(raw[1][i].strip()))
	return nums


def findPossibilities(nums):
	possibilities = []
	for a in nums:
		for b in nums:
			for c in nums:
				for d in nums:
					for e in nums:
						possibilities.append([a,b,c,d,e])
	return possibilities


def findPartialProducts(possibilities, nums):
	answers = 0
	for elem in possibilities:
		alldigits = ""
		abc = int(str(elem[0]) + str(elem[1]) + str(elem[2]))
		de = int(str(elem[3]) + str(elem[4]))

		if len(str(elem[3] * abc)) == 3 and len(str(elem[4] * abc)) == 3:
			alldigits += str(elem[3] * abc)
			alldigits += str(elem[4] * abc)
			alldigits += str(abc*de)
			check = True
			if len(str(abc*de)) == 4:
				for elem2 in alldigits:
					if int(elem2) not in nums:
						check = False
				if check:
					answers += 1

	return answers

def writeOutput(answers):
	with open("crypt1.out", "w+") as f:
		f.write(str(answers) + "\n")
nums = readInput()

possibilities = findPossibilities(nums)

answers = findPartialProducts(possibilities, nums)

writeOutput(answers)


#read and start ski course






































#sorted(list)
#5^6 == 5**6
