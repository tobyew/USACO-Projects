#http://www.usaco.org/index.php?page=viewproblem2&cpid=567
def readInput():
	with open("paint.in", "r") as f:
		inp = f.readlines()
	fjmin = int(inp[0].strip().split()[0])
	fjmax = int(inp[0].strip().split()[1])
	bessiemin = int(inp[1].strip().split()[0])
	bessiemax = int(inp[1].strip().split()[1])
	return fjmin, fjmax, bessiemin, bessiemax


def paint(fjmin, fjmax, bessiemin, bessiemax):
	painted = set()
	for i in range(fjmin, fjmax):
		painted.add(i)
	for i in range(bessiemin, bessiemax):
		painted.add(i)
	print(painted)
	return (len(painted))


def output(answer):
	with open("paint.out", "w+") as f:
		f.write(str(answer) + "\n")
fjmin, fjmax, bessiemin, bessiemax = readInput()
answer = paint(fjmin, fjmax, bessiemin, bessiemax)
output(answer)
