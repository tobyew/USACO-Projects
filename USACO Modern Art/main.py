#http://www.usaco.org/index.php?page=viewproblem2&cpid=737
def readInput():
	with open("art.in", "r") as f:
		inp = f.readlines()
	size = int(inp[0].strip())
	canvas = []
	for i in range(size):
		canvas.append(inp[i+1].strip())
	return canvas


def findColors(canvas):
	colors = set()
	for elem in canvas:
		for letter in elem:
			colors.add(int(letter))
	if 0 in colors:
		colors.remove(0)
	return colors

def findxy(num, squaresize):
	y = int((int(num)/int(squaresize))+1)
	x = int((int(num)%int(squaresize))+1)
	return x,y

def findx(num, squaresize):
	x = int((int(num)%int(squaresize))+1)
	return x

def findy(num, squaresize):
	y = int((int(num)/int(squaresize))+1)
	return y

def findRects(canvas, colors):
	squaresize = len(canvas)
	rectCoords = {}

	for color in colors:
		top = -1
		bottom = -1
		left = 100
		right = -1
		counter = -1
		for elem in canvas:
			for letter in elem:
				counter += 1
				if int(letter) == color:
					if top == -1:
						top = counter
						#print("1", counter)
					if findy(bottom, squaresize) < findy(counter, squaresize):
						bottom = counter
						#print("2", counter)
					if findx(left, squaresize) < findx(counter, squaresize):
						left = counter
						#print("3", counter)
					if findx(right, squaresize) > findx(counter, squaresize):
						right = counter
						#print("4", counter)
		coord1 = [findx(right, squaresize), findy(top, squaresize)]
		coord2 = [findx(left, squaresize), findy(bottom, squaresize)]
		rectCoords[color] = [coord1, coord2]
	return rectCoords

def inRect(color, counter, rectCoords):
	squaresize = len(canvas)
	if rectCoords[color][0][0] <= findx(counter, squaresize) <= rectCoords[color][1][0]:
		if rectCoords[color][0][1] <= findy(counter, squaresize) <= rectCoords[color][1][1]:
			return True
	

def findAnswer(canvas, colors, rectCoords):
	possibilities = set()
	possibilities = colors.copy()
	for color in colors:
		counter = -1
		for elem in canvas:
			for letter in elem:
				counter += 1
				if inRect(color, counter, rectCoords):
					if str(letter) != str(color):
						if int(letter) in possibilities:
							possibilities.remove(int(letter))
	return possibilities

def output(answer):
	with open("art.out", "w+") as f:
		f.write(str(len(answer)) + "\n")
canvas = readInput()
colors = findColors(canvas)
rectCoords = findRects(canvas, colors)
answer = findAnswer(canvas, colors, rectCoords)
output(answer)
#finish this
