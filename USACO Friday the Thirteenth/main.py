#https://train.usaco.org/usacoprob2?a=fxKXvyWsW9y&S=friday
"""
ID: tobyewo1
LANG: PYTHON3
TASK: friday
"""
result = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
#sat sun mon...
with open("friday.in", "r") as f:
	duration = int(f.read())
daysOfMonth = {1: 31, 2: 28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

day = 2
startYear = 1900
endYear = startYear + duration

for i in range(startYear, endYear):
	daysOfMonth[2] = 28
	if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
		daysOfMonth[2] = 29
	for month in daysOfMonth:
		for date in range(daysOfMonth[month]):
			if date == 12:
				result[day] += 1
			day += 1
			day %= 7


resultString = ''
for elem in result:
	if elem == 6:
		resultString += str(result[elem])
	else:
		resultString += str(result[elem]) + " "
with open("friday.out", "w+") as f:
	f.write(resultString + "\n")
