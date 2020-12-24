#http://www.usaco.org/index.php?page=viewproblem2&cpid=665


def readInput():
	with open("cowsignal.in", "r") as f:
		raw = f.readlines()
	firstLine = raw[0].strip().split()
	height = firstLine[0]
	width = firstLine[1]
	scale = int(firstLine[2])
	firstPattern = []
	for i in range(len(raw)-1):
		firstPattern.append(raw[i+1].strip())
	return height, width, scale, firstPattern
def math(height, width, scale, firstPattern):
	newPattern = []
	for line in firstPattern:
		tempNewLine = ""
		for letter in line:
			for i in range(scale):
				tempNewLine += letter	
		for i in range(scale):
			newPattern.append(tempNewLine)
	return newPattern

def output(newPattern):
	with open("cowsignal.out", "w+") as f:
		output = ''
		for elem in newPattern:
			output += elem + "\n"
		f.write(output)

height, width, scale, firstPattern = readInput()
newPattern = math(height, width, scale, firstPattern)
output(newPattern)
