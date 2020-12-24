with open("square.in", "r") as f:
	theInput = f.readlines()
	
print(theInput)
xcoords = []
xcoords.append(int(theInput[0][0]))
xcoords.append(int(theInput[0][4]))
xcoords.append(int(theInput[1][0]))
xcoords.append(int(theInput[1][4]))
print(xcoords)


ycoords = []
ycoords.append(int(theInput[0][2]))
ycoords.append(int(theInput[0][6]))
ycoords.append(int(theInput[1][2]))
ycoords.append(int(theInput[1][6]))
print(ycoords)


maxx = max(xcoords)
maxy = max(ycoords)
minx = min(xcoords)
miny = min(ycoords)

length = maxy - miny
width = maxx - minx

output = 0

if length > width:
	output=length*length
else:
	output=width*width

with open("square.out", "w+") as f:
	f.write(str(output))
