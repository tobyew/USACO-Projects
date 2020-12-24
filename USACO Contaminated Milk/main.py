#http://www.usaco.org/index.php?page=viewproblem2&cpid=569
def readInput():
	with open("badmilk.in", "r") as f:
		inp = f.readlines()
	friends = int(inp[0].strip().split()[0])
	milkflavors = int(inp[0].strip().split()[1])
	drank = int(inp[0].strip().split()[2])
	sick = int(inp[0].strip().split()[3])
	inpdrank = inp[1:1+drank]
	inpsick = inp[1+drank:]
	return friends, milkflavors, drank, sick, inpdrank, inpsick

def formatInput(friends, milkflavors, drank, sick, inpdrank, inpsick):
	#person may drink the same milk multiple times
	milklogs = {}
	for i in range(1, milkflavors+1):
		milklogs[i] = []
	for elem in inpdrank:
		elem = elem.strip()
		milklogs[int(elem.split()[1])].append((int(elem.split()[0]), int(elem.split()[2])))

	sicklogs = {}
	for elem in inpsick:
		sicklogs[int(elem.strip().split()[0])] = int(elem.strip().split()[1])

	return milklogs, sicklogs


def dropit(friends, milkflavors, drank, sick, inpdrank, inpsick, milklogs, sicklogs):
	'''
	badmilk_maybe = set()
	for milk in milklogs:
		for persontuple in milklogs[milk]:
			if persontuple[0] in sicklogs:
				if persontuple[1] <= sicklogs[persontuple[0]]:
					badmilk_maybe.add(milk)

	'''

	whogotsick = []
	for i in range(1, friends+1):
		if i in sicklogs:
			whogotsick.append(i)
	counterpeople = set()
	print(whogotsick)
	badmilk_maybe_2 = set()
	for milk in milklogs:
		counter = 0
		for tuple in milklogs[milk]:
			print(tuple)
			if tuple[0] in whogotsick:
				print("ho")
				if tuple[1] < sicklogs[tuple[0]]:
					print("to")
					if tuple[0] not in counterpeople:
						counter += 1
					counterpeople.add(tuple[0])
					
		print("counter", counter)
		print("whogotsick", whogotsick)
		if counter == len(whogotsick):
			badmilk_maybe_2.add(milk)

	whodrankwhat = {}
	wdwpeople = set()
	print(milklogs)
	print(badmilk_maybe_2)
	for badmilk in badmilk_maybe_2:
		print("badmilk", badmilk)
		whodrankwhat[badmilk] = 0
		for milk in milklogs[badmilk]:
			print("milk", milk)
			if milk[0] not in wdwpeople:
				whodrankwhat[badmilk] += 1
			wdwpeople.add(milk[0])
	print(whodrankwhat)
	return whodrankwhat


def writeOutput(whodrankwhat):
	print(whodrankwhat)
	answer = str(max(whodrankwhat.values())) + "\n"
	with open("badmilk.out", "w+") as f:
		f.write(answer)
friends, milkflavors, drank, sick, inpdrank, inpsick = readInput()

milklogs, sicklogs = formatInput(friends, milkflavors, drank, sick, inpdrank, inpsick)

whodrankwhat = dropit(friends, milkflavors, drank, sick, inpdrank, inpsick, milklogs, sicklogs)

writeOutput(whodrankwhat)


#try to fix for homework (number six and number nine)
#otherwise do usaco january 2016 (next on prpoblem list) (promotion counting)
