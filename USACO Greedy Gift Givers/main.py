"""
ID: tobyewo1
LANG: PYTHON3
TASK: gift1
"""
with open("gift1.in", "r") as f:
	theInput = f.readlines()
num_people = int(theInput[0])
theInput.pop(0)
balances = {}
for i in range(num_people):
	balances[theInput[0].strip()] = 0
	theInput.pop(0)


for i in range(num_people):
	giver = theInput[0]
	theInput.pop(0)
	num_getters = int(theInput[0].split()[1])
	if num_getters != 0:
		remainder = int(theInput[0].split()[0])%num_getters
		amount_per_getter = int(int(theInput[0].split()[0]) / num_getters)
	else:
		remainder = int(theInput[0].split()[0])
		amount_per_getter = 0
	theInput.pop(0)
	for i in range(num_getters):
		balances[theInput[0].strip()] += amount_per_getter
		theInput.pop(0)

	balances[giver.strip()] -= (amount_per_getter * num_getters) #- remainder

#output
output = ''
for elem in balances:
	output += (str(elem) + " " + str(balances[elem]) + "\n")

with open("gift1.out", "w+") as f:
	f.write(output)

#debug and submit the following (+this one probably, i forget)
'''
solutions:
https://repl.it/@JuniLearning/UB3-Friday-the-Thirteenth
 https://repl.it/@JuniLearning/UB4-Broken-Necklace

'''
