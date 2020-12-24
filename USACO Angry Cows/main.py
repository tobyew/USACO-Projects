#http://www.usaco.org/index.php?page=viewproblem2&cpid=592
import copy

def readInput():
	with open("angry.in", "r") as f:
		inp = f.readlines()
	alist = []
	for elem in inp:
		alist.append(int(elem.strip()))
	alist.sort()
	field = {}
	for i in range(min(alist), max(alist)+1):
		if i in alist:
			field[i] = True
		else:
			field[i] = False
	return field


def checkEach(field):
	field_memory = copy.deepcopy(field)
	print()
	score = 0
	for bale in field:
		#this checks if theres actually something there
		print(field)
		if field[bale]:
			currentBale = bale
			explosionradius = 0
			lscore = 1
			lchaining = True
			while lchaining:
				explosionradius += 1
				lowest = 1000000001
				isBale = False
				for i in range(1,explosionradius+1):
					#this makes sure its above the lowest
					if (currentBale - i) >= min(field.keys()):
						if field[currentBale - i]:
							field[currentBale - i] = False
							isBale = True
							lscore += 1
							if lowest > currentBale - i:
								lowest = currentBale-i
				if not isBale:
					lchaining = False
				currentBale = lowest
			#print()
				#how do i split
			#print(lscore)
			

			currentBale = bale
			explosionradius = 0
			rscore = 0
			rchaining = True

			while rchaining:
				explosionradius += 1
				highest = -1
				isBale = False
				for i in range(1,explosionradius+1):
					#this makes sure its above the highest
					#fix: after 2 hours, it was the >=, not >
					if (currentBale + i) <= max(field.keys()):
						if field[currentBale + i]:
							field[currentBale + i] = False
							isBale = True
							rscore += 1
							if highest < currentBale + i:
								highest = currentBale+i
				if not isBale:
					rchaining = False
				currentBale = highest
			#print()
				#how do i split
			#print(score)
		
		print(rscore+lscore)
		print(bale)
		print(field)
		print("\n")
		field = copy.deepcopy(field_memory)
		if score < rscore + lscore:
			score = rscore + lscore
	return score


def output(score):
	with open("angry.out", "w+") as f:
		print(score)
		f.write(str(score) + "\n")

field = readInput()
score = checkEach(field)
print(field)
output(score)

#debug (deepcopy copy false copy deep)
#bug- 3.in answer is 11 but we got 12 with 34
