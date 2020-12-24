#http://www.usaco.org/index.php?page=viewproblem2&cpid=688
'''
ID: tobyewo1
LANG: PYTHON3
TASK: hps
'''
possibilites = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
def readInput():
	with open("hps.in", "r") as f:
		inp = f.readlines()
	numgames = int(inp[0].strip())
	games = []
	for i in range(numgames):
		games.append([int(inp[i+1].strip().split()[0]), int(inp[i+1].strip().split()[1])])
	return games


def joe(games):
	answer = -1
	for rotation in possibilites:
		wins = 0
		for elem in games:
			if rotation.index(elem[1]) - rotation.index(elem[0]) == 1 or rotation.index(elem[1]) - rotation.index(elem[0]) == -2:
				wins += 1
		if wins > answer:
			answer = wins

	return answer

def output(answer):
	with open("hps.out", "w+") as f:
		f.write(str(answer) + "\n")
games = readInput()
answer = joe(games)
output(answer)
