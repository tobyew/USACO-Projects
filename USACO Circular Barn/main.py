#http://www.usaco.org/index.php?page=viewproblem2&cpid=616
#29 is number of cows
#draw it out
def readInput():
	with open("cbarn.in", "r") as f:
		inp = f.readlines()
	rooms = []
	inp.pop(0)
	for elem in inp:
		rooms.append(int(elem.strip()))
	return rooms

def tryrooms(rooms):
	highest = 100000000000
	numrooms = len(rooms)
	for i in range(numrooms):
		print(rooms[i])
		movedcows = 0
		cows = sum(rooms)
		iter = i
		for room in range(numrooms):
			movedcows += cows
			cows -= rooms[int(i+room)]	
			print(rooms[int(i+room)], cows)
		if highest > movedcows-sum(rooms):
			highest = movedcows-sum(rooms)
	return highest

def output(highest):
	with open("cbarn.out", "w+") as f:
		f.write(str(highest) + "\n")



rooms = readInput()
highest = tryrooms(rooms)
output(highest)
#work on http://www.usaco.org/index.php?page=viewproblem2&cpid=617 (go by n, so sort of brute force) time myself
