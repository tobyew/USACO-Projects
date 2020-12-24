#http://www.usaco.org/index.php?page=viewproblem2&cpid=689
'''
ID: tobyewo1
LANG: PYTHON3
TASK: cowtip
'''
def readInput():
	with open("cowtip.in", "r") as f:
		inp = f.readlines()
	squaresize = int(inp[0].strip())
	lines = {}
	for i in range(squaresize):
		ist = []
		for elem in inp[i+1].strip():
			ist.append(elem)
		lines[str(i)] = ist
	return lines, squaresize

def findHighest(lines, squaresize):
	highest = -1
	counter = 0
	for i in range(squaresize):
		line = lines[str(i)]
		for cow in line:
			if cow == '1':
				highest = counter

			counter += 1
	return highest
			
def findxy(num, squaresize):
	y = int((int(num)/int(squaresize))+1)
	x = int((int(num)%int(squaresize))+1)
	return x,y



def bob(lines, squaresize):
	answer = -1
	highest = 0
	while highest != -1:
		answer += 1
		highest = findHighest(lines, squaresize)
		x,y = findxy(highest, squaresize)
		for i in range(squaresize):
			line = lines[str(i)]
			for cowindex in range(squaresize):
				tempx, tempy = findxy(cowindex+(i*squaresize), squaresize)
				if tempx <= x and tempy <= y:
					if lines[str(tempy-1)][tempx-1] == '1':
						lines[str(tempy-1)][tempx-1] = '0'
					elif lines[str(tempy-1)][tempx-1] == '0':
						lines[str(tempy-1)][tempx-1] = '1'
	return answer
		

def writeOutput(answer):
	with open("cowtip.out", "w+") as f:
		f.write(str(answer)+"\n")

lines, squaresize = readInput()

answer = bob(lines, squaresize)

writeOutput(answer)


#homework: http://www.usaco.org/index.php?page=viewproblem2&cpid=735
