#https://train.usaco.org/usacoprob2?a=fxKXvyWsW9y&S=transform
'''
ID: tobyewo1
LANG: PYTHON3
TASK: transform
'''

def readInput():
	first_pattern = []
	second_pattern = []
	raw = []
	with open("transform.in", "r") as f:
		for elem in f.readlines():
			raw.append(elem.strip())
		length_squares = int(raw[0])
		raw.pop(0)
		counter = 0
		for elem in raw:
			counter += 1
			for letter in elem:
				if counter > length_squares:
					second_pattern.append(letter.strip())
				else:
					first_pattern.append(letter.strip())
				

	return first_pattern, second_pattern, length_squares


def rotate90(first_pattern, length_squares):
	new_pattern = []
	for i in range(length_squares*length_squares):
		new_pattern.append("t")
	for i in range(len(first_pattern)):
		col = i%length_squares
		row = int(i/length_squares)
		new_row = col
		new_col = length_squares-row-1
		newIndex = new_row * length_squares + new_col
		new_pattern[newIndex] = first_pattern[i]
	return new_pattern

def reflect(first_pattern, length_squares):
	new_pattern = []
	for i in range(length_squares*length_squares):
		new_pattern.append("t")
	for i in range(len(first_pattern)):
		col = i%length_squares
		row = int(i/length_squares)
		new_row = row
		new_col = length_squares-col-1
		newIndex = new_row * length_squares + new_col
		new_pattern[newIndex] = first_pattern[i]
	'''
	new_pattern = []
	for i in range(length_squares*length_squares):
		new_pattern.append("t")
	for row in range(length_squares):
		beginning_of_row = int(row*length_squares)
		current_row = []

		for i in range(length_squares):
			current_row.append(first_pattern[int(beginning_of_row)+i])

		new_row = []
		for i in range(int(len(current_row))):
			new_row.append(current_row[length_squares-i-1])

		for i in range(length_squares):
			new_pattern[beginning_of_row+i] = new_row[i]
		'''
	return new_pattern
def main():
	originalPattern, newPattern, length_squares = readInput()

	fout = open('transform.out', 'w')
	rotate90pattern = rotate90(originalPattern, length_squares)
	rotate180pattern = rotate90(rotate90(originalPattern, length_squares), length_squares)
	rotate270pattern = rotate90(rotate90(rotate90(originalPattern, length_squares), length_squares), length_squares)
	reflectPattern = reflect(originalPattern, length_squares)
	print(rotate90(reflectPattern, length_squares))
	if newPattern == rotate90pattern:
		fout.write("1\n")
	elif newPattern == rotate180pattern:
		fout.write("2\n")
	elif newPattern == rotate270pattern:
		fout.write("3\n")
	elif newPattern == reflectPattern:
		fout.write("4\n")
	elif newPattern == rotate90(reflectPattern, length_squares):
		fout.write("5\n")
	elif newPattern == rotate90(rotate90(reflectPattern, length_squares), length_squares):
		fout.write("5\n")
	elif newPattern == rotate90(rotate90(rotate90(reflectPattern, length_squares), length_squares), length_squares):
		fout.write("5\n")
	elif newPattern == originalPattern:
		fout.write("6\n")
	else:
		fout.write("7\n")

main()

#read through the mixing milk problem and try to finish
