#http://www.usaco.org/index.php?page=viewproblem2&cpid=568
def readInput():
	with open("speeding.in", "r") as f:
		inp = f.readlines()
		n = int(inp[0].strip().split()[0])
		m = int(inp[0].strip().split()[1])
	nslens = []
	nsspeed = []
	mslens = []
	msspeed = []
	for i in range(n):
		nslens.append(inp[i+1].strip().split()[0])
		nsspeed.append(inp[i+1].strip().split()[1])
	for i in range(m):
		mslens.append(inp[i+1+n].strip().split()[0])
		msspeed.append(inp[i+1+n].strip().split()[1])
	return inp, nslens, mslens, nsspeed, msspeed

def makeList(inp, nslens, mslens, nsspeed, msspeed):
	nslist = []
	mslist = []
	counter = -1
	for elem in nslens:
		counter += 1
		for i in range(int(elem)):
			nslist.append(nsspeed[counter])

	counter = -1
	for elem in mslens:
		counter += 1
		for i in range(int(elem)):
			mslist.append(msspeed[counter])
	return nslist, mslist


def findAnswer(inp, nslist, mslist, nsspeed, msspeed):
	answer = 0
	for i in range(100):
		if int(mslist[i]) - int(nslist[i]) > int(answer):
			answer = int(mslist[i]) - int(nslist[i])
			print(i)
			print(mslist, nslist)
	return answer

def writeOutput(answer):
	with open("speeding.out", "w+") as f:
		f.write(str(answer) + "\n")



inp, nslens, mslens, nsspeed, msspeed = readInput()

nslist, mslist = makeList(inp, nslens, mslens, nsspeed, msspeed)

answer = findAnswer(inp, nslist, mslist, nsspeed, msspeed)

writeOutput(answer)
	
	#finish
