#https://train.usaco.org/usacoprob2?a=fxKXvyWsW9y&S=milk
'''
ID: tobyewo1
LANG: PYTHON3
TASK: milk
'''
def readInput():
	with open("milk.in", "r") as f:
		raw = f.readlines()
		firstNumbers = raw[0].strip().split()
		farmers = int(firstNumbers[1])
		wantedMilk = firstNumbers[0]
		farmerData = {}
		for i in range(1, farmers+1):
			price = int(raw[i].strip().split()[0])
			units = int(raw[i].strip().split()[1])
			if price in farmerData:
				farmerData[price] = farmerData[price]+units
			else:
				farmerData[price] = units
	return farmers, int(wantedMilk), farmerData

	
def maths(farmers, wantedMilk, farmerData):
	milkBought = 0
	moneySpent = 0
	for key in sorted(farmerData.keys()):
		if milkBought + farmerData[key] > wantedMilk:
			print("here1")
			save = wantedMilk - milkBought
			moneySpent += save*key
			break
		else:
			print("here2")
			milkBought += farmerData[key]
			moneySpent += key*farmerData[key]
			if milkBought == wantedMilk:
				break
	return moneySpent



def output(moneySpent):
	with open("milk.out", "w+") as f:
		f.write(str(moneySpent) + "\n")

farmers, wantedMilk, farmerData = readInput()
moneySpent = maths(farmers, wantedMilk, farmerData)
output(moneySpent)

#do barn repair
#find top m-1 gaps
#do
