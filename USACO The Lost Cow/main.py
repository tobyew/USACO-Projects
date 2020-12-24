#http://www.usaco.org/index.php?page=viewproblem2&cpid=735
def readInput():
	with open("lostcow.in", "r") as f:
		raw = f.readlines()
		fj = raw[0].strip().split()[0]
		bessie = raw[0].strip().split()[1]
	return int(fj), int(bessie)
def bob(fj, bessie):
	fjpos = fj
	increment = 1
	distWalked = 0
	while True:
		oldpos = fjpos
		fjpos = fj+increment
		distWalked += abs(oldpos-fjpos)
		
		
		if fjpos == bessie:
			return distWalked
		elif fj < bessie and fjpos > bessie:
			overness = abs(fjpos - bessie)
			print(distWalked)
			print(overness)
			return distWalked - overness
		elif fj > bessie and fjpos < bessie:
			overness = abs(fjpos - bessie)
			print(distWalked)
			print(overness)
			return distWalked - overness

		increment *= -2

def writeOutput(answer):
	with open("lostcow.out", "w+") as f:
		f.write(str(answer) + "\n")
fj, bessie = readInput()
distWalked = bob(fj, bessie)
writeOutput(distWalked)

#http://www.usaco.org/index.php?page=viewproblem2&cpid=736
#sets!
