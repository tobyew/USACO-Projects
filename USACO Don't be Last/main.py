#http://www.usaco.org/index.php?page=viewproblem2&cpid=688
'''
ID: tobyewo1
LANG: PYTHON3
TASK: notlast
'''

cows = {"Bessie":0, "Elsie":0, "Daisy":0, "Gertie":0, "Annabelle":0, "Maggie":0, "Henrietta":0}

def readInput():
	with open("notlast.in", "r") as f:
		inp = f.readlines()
		records = int(inp[0].strip())
		for i in range(records):
			cows[inp[i+1].strip().split()[0]] += int(inp[i+1].strip().split()[1])

def findSecond():
	numbers = sorted(list(set(cows.values())))
	if len(numbers) == 1:
		return "Tie"
	secondValue = numbers[1]
	answer = ''
	for cow in cows:
		if cows[cow] == secondValue:
			if answer == '':
				answer = cow
			else:
				answer = 'Tie'
				return answer
	return answer

def output(answer):
	with open("notlast.out", "w+") as f:
		f.write(answer + "\n")

readInput()
answer = findSecond()
output(answer)
