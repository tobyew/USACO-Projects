#https://train.usaco.org/usacoprob2?a=fxKXvyWsW9y&S=skidesign
'''
ID: tobyewo1
LANG: PYTHON3
TASK: skidesign
'''
def readInput():
	with open("skidesign.in", "r") as f:
		raw = f.readlines()
		numhills = int(raw[0].strip())
		hillheights = []
		for i in range(1,numhills+1):
			hillheights.append(int(raw[i].strip()))
	return numhills, sorted(hillheights)


def calcOutput(numhills, hillheights):
	bottomRange = hillheights[0]
	topRange = bottomRange + 17
	car = []
	while bottomRange <= hillheights[-1] - 17:
		tempCost = 0
		for elem in hillheights:
			if elem > topRange:
				tempCost += (topRange - elem) ** 2
			elif elem < bottomRange:
				tempCost += (bottomRange - elem) ** 2
		car.append(tempCost)
		bottomRange += 1
		topRange += 1
	return str(min(car))

def output(yee):
	with open("skidesign.out", "w+") as f:
		f.write(yee + "\n")
numhills, hillheights = readInput()
output(calcOutput(numhills, hillheights))


#http://www.usaco.org/index.php?page=viewproblem2&cpid=664
#start and maybe finish


#readinput
#countletterrsinword
#math
#output
'''
USACO 2016 December Contest, Bronze
Problem 2. Block Game
'''
