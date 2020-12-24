#https://train.usaco.org/usacoprob2?a=fxKXvyWsW9y&S=combo
'''
ID: tobyewo1
LANG: PYTHON3
TASK: combo
'''
def readInput():
	with open("combo.in", "r") as f:
		raw = f.readlines()
		for i in range(len(raw)):
			raw[i] = raw[i].strip()
	farmerCombo = raw[1].split()
	masterCombo = raw[2].split()
	for i in range(3):
		farmerCombo[i] = int(farmerCombo[i])
		masterCombo[i] = int(masterCombo[i])
	lockSize = raw[0]
	return lockSize, farmerCombo, masterCombo






def calcOtherCombos(lockSize, farmerCombo, masterCombo):
	nums = []
	for i in range(1, int(lockSize)+1):
		nums.append(i)
	mcombos = set()
	masterAsStr = ""
	for i in range(len(masterCombo)):
		masterAsStr += str(masterCombo[i]) + " "
	first_center = masterCombo[0]
	second_center = masterCombo[1]
	third_center = masterCombo[2]
	firsts = []
	seconds = []
	thirds = []
	for i in range(-2,3):
		firsts.append(nums[(first_center + i)%len(nums)] - 1)
		seconds.append(nums[(second_center + i)%len(nums)] - 1)
		thirds.append(nums[(third_center + i)%len(nums)] - 1)
	

	for third in thirds:
		for second in seconds:
			for first in firsts:
				mcombos.add(str(first) + " " + str(second) + " " + str(third))

	farmerAsStr = ""
	for i in range(len(farmerCombo)):
		farmerAsStr += str(farmerCombo[i]) + " "
	fcombos = set()
	first_center = farmerCombo[0]
	second_center = farmerCombo[1]
	third_center = farmerCombo[2]
	firsts = []
	seconds = []
	thirds = []
	for i in range(-2,3):
		firsts.append(nums[(first_center + i)%len(nums)] - 1)
		seconds.append(nums[(second_center + i)%len(nums)] - 1)
		thirds.append(nums[(third_center + i)%len(nums)] - 1)
	for third in thirds:
		for second in seconds:
			for first in firsts:
				fcombos.add(str(first) + " " + str(second) + " " + str(third))

	#print(mcombos)
	#print(fcombos.union(mcombos))
	return len(fcombos.union(mcombos))


def output(deoutput):
	with open("combo.out", "w+") as f:
		f.write(str(deoutput) + "\n")



lockSize, farmerCombo, masterCombo = readInput()

deoutput = calcOtherCombos(lockSize, farmerCombo, masterCombo)

output(deoutput)

#rewrite, debug
#look at mod thing (below)
#a[5%len(a)]


