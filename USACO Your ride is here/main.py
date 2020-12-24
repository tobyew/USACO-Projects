#https://train.usaco.org/usacoprob2?a=fxKXvyWsW9y&S=ride
"""
ID: tobyewo1
LANG: PYTHON3
TASK: ride
"""
with open("ride.in", "r") as f:
	theInput = f.readlines()
cometName = theInput[0].strip()
groupName = theInput[1].strip()
cnv = 1
gnv = 1
for i in range(len(cometName)):
	cnv *= ord(cometName[i]) - 64
for i in range(len(groupName)):
	gnv *= ord(groupName[i]) - 64
if cnv%47 == gnv%47:
	output = 'GO\n'
else:
	output = 'STAY\n'
with open("ride.out", "w") as f:
	f.write(output)
