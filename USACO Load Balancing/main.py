#http://www.usaco.org/index.php?page=viewproblem2&cpid=617
def readInput():
	with open("balancing.in", "r") as f:
		inp = f.readlines()
	squaresize = int(inp[0].strip().split()[1])
	numcows = int(inp[0].strip().split()[0])
	inp.pop(0)
	cows = []
	for elem in inp:
		cows.append((int(elem.strip().split()[0]), int(elem.strip().split()[1])))
	print(squaresize, numcows, cows)
	return squaresize, numcows, cows


def find(squaresize, numcows, cows):
	highest = 18371241384
	fencexs = []
	fenceys = []
	for fencecow in cows:
		x = fencecow[0]
		y = fencecow[1]
		#if fence wouold be in the grid
		if squaresize < x+1:
			fencexs.append(x-1)
		else:
			fencexs.append(x+1)
			
		if squaresize < y+1:
			fenceys.append(y-1)
		else:
			fenceys.append(y+1)
	print(fencexs, fenceys)
		#these vars will count cows on each side
	for x in fencexs:
		for y in fenceys:
			topleft = 0
			topright = 0
			bottomleft = 0
			bottomright = 0
			#print(fencecow)
			for cow in cows:
				if cow[0] < x and cow[1] < y:
					bottomleft += 1
					#print("bl ", cow)
				elif cow[0] > x and cow[1] < y:
					bottomright += 1
					#print("br ", cow)
				elif cow[0] < x and cow[1] > y:
					topleft += 1
					#print("tl ", cow)
				elif cow[0] > x and cow[1] > y:
					topright += 1
					#print("tr ", cow)
			if max(topleft, topright,bottomleft, bottomright) < highest:
				highest = max(topleft, topright, bottomleft, bottomright)
				fencecoords = (x, y)
	#print(fencecoords)
	return highest
		
def output(highest):
	with open("balancing.out", "w+") as f:
		f.write(str(highest) + "\n")
squaresize, numcows, cows = readInput()
highest = find(squaresize, numcows, cows)
output(highest)
#create a list of all fencex and fencey and then try all possibilities:
#fencex: [1,3,5,7]
#fencey: [2,4,6,8]
#1,2 1,4 1,6 3,2 
