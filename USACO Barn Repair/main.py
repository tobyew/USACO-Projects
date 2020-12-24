#https://train.usaco.org/usacoprob2?a=fxKXvyWsW9y&S=barn1
'''
ID: tobyewo1
LANG: PYTHON3
TASK: barn1
'''
def readInput():
	with open("barn1.in", "r") as f:
		raw = f.readlines()
		firstLine = raw[0].strip().split()
		numBoards = int(firstLine[0])
		numStalls = int(firstLine[1])
		numCows = int(firstLine[2])
		occupiedStalls = []
		for i in range(1, len(raw)):
			occupiedStalls.append(int(raw[i].strip()))
		firstCow = min(occupiedStalls)
		lastCow = max(occupiedStalls)
		occupiedStalls = sorted(occupiedStalls)
	return occupiedStalls, numBoards, numStalls, firstCow, lastCow, firstLine



def calcGapLengths(occupiedStalls):
	gapLengths = []
	for i in range(len(occupiedStalls)-1):
		potentialgap = occupiedStalls[i+1] - occupiedStalls[i]
		gapLengths.append(potentialgap)
	return sorted(gapLengths)

def calcNumStallsBlocked(occupiedStalls, gapLengths, numBoards, firstCow, lastCow):
	biggestGaps = []
	for i in range(numBoards-1):
		biggestGaps.append(gapLengths[-(i+1)])
	croppedStalls = lastCow-firstCow + 1
	output = croppedStalls-sum(biggestGaps)+len(biggestGaps)
	return output


def writeOutput(output):
	with open("barn1.out", "w+") as f:
		f.write(str(output) + "\n")

occupiedStalls, numBoards, numStalls, firstCow, lastCow, firstLine = readInput()
if int(firstLine[0]) > int(firstLine[2]):
	writeOutput(int(firstLine[2]))
else:
	gapLengths = calcGapLengths(occupiedStalls)

	numBlocked = calcNumStallsBlocked(occupiedStalls, gapLengths, numBoards, firstCow, lastCow)
	writeOutput(numBlocked)

	#do combination lock
