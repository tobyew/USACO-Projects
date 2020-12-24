#http://www.usaco.org/index.php?page=viewproblem2&cpid=736
def readInput():
	with open("cownomics.in", "r") as f:
		inp = f.readlines()
		num_of_each = int(inp[0].strip().split()[0])
		length = int(inp[0].strip().split()[1])
	spotted = {}
	not_spotted = {}
	for i in range(num_of_each):
		spotted[i] = inp[i+1].strip()
		not_spotted[i] = inp[i+num_of_each+1].strip()
	print(spotted)
	print(not_spotted)
	return num_of_each, length, spotted, not_spotted



def getSets(num_of_each, length, spotted, not_spotted,):
	#if all spotted cows[i] is not in all unspotted cows[i]
	count = -1
	spotSets = []
	unspotSets = []
	for i in range(length):
		spotSets.append(set())
		unspotSets.append(set())
	for elem in spotted:
		for letter in spotted[elem]:
			count += 1
			spotSets[count%length].add(letter)
	for elem in not_spotted:
		for letter in not_spotted[elem]:
			count += 1
			unspotSets[count%length].add(letter)
	print(spotSets, unspotSets)
	return spotSets, unspotSets


def unique(num_of_each, length, spotted, not_spotted, spotSets, unspotSets):
	answer = 0
	for i in range(length):
		if len(spotSets[i]) + len(unspotSets[i]) == len(spotSets[i].union(unspotSets[i])):
			answer += 1
	return answer

def output(answer):
	with open("cownomics.out", "w+") as f:
		f.write(str(answer) + "\n")

num_of_each, length, spotted, not_spotted = readInput()
spotSets, unspotSets = getSets(num_of_each, length, spotted, not_spotted)
answer = unique(num_of_each, length, spotted, not_spotted, spotSets, unspotSets)
output(answer)
