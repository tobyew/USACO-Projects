#http://www.usaco.org/index.php?page=viewproblem2&cpid=591
def readInput():
	with open("promote.in", "r") as f:
		inp = f.readlines()
	bronze = [int(inp[0].strip().split()[0]), int(inp[0].strip().split()[1])]
	silver = [int(inp[1].strip().split()[0]), int(inp[1].strip().split()[1])]
	gold = [int(inp[2].strip().split()[0]), int(inp[2].strip().split()[1])]
	platinum = [int(inp[3].strip().split()[0]), int(inp[3].strip().split()[1])]
	return bronze, silver, gold, platinum



def myway(bronze, silver, gold, platinum):
	sd = silver[1]-silver[0]
	gd = gold[1]-gold[0]
	pd = platinum[1]-platinum[0]
	num1 = 0
	num2 = 0
	num3 = 0
	num1 += pd + gd + sd
	num2 += pd + gd
	num3 += pd
	return num1, num2, num3

def output(num1, num2, num3):
	with open("promote.out", "w+") as f:
		f.write(str(num1) + "\n" + str(num2) + "\n" + str(num3) + "\n")

bronze, silver, gold, platinum = readInput()
num1, num2, num3 = myway(bronze, silver, gold, platinum)
output(num1, num2, num3)

#dict
#http://www.usaco.org/index.php?page=viewproblem2&cpid=592
#angry burd
