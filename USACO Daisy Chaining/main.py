#http://usaco.org/index.php?page=viewproblem2&cpid=1060
import itertools


def doinput():
	numpics = int(input())
	temppics = input()

	pics = []
	for i in range(numpics):
		pics.append(temppics.split()[i])

	#print(pics)
	return pics, numpics






def findcombos(pics, numpics):
	#combos = []
	#for i in range(numpics):
	#	for combo in itertools.combinations(pics, i):
	#		if len(combo) != 0:
	#			newcombo = []
	#			for elem in combo:
	#				newcombo.append(int(elem.replace(",", "")))
	#			combos.append(newcombo)
	
	combos = []
	for i in range(numpics+1):
		for j in range(i, numpics+1):
			if len(pics[i:j]) >= 1:
				combos.append(pics[i:j])
			#print(i, j)

	newcombos = []
	for dlist in combos:
		newelem = []
		for elem in dlist:
			newelem.append(int(elem))
		newcombos.append(newelem)
	combos = newcombos
	print(combos)
	return combos



def testcombos(combos):
	#print("\n\n\n")
	total = 0
	for elem in combos:
		average = float(sum(elem)) / float(len(elem))
		#print(elem)
		#print(average)

		
		if average in elem:
			total += 1
			#print("----", total)
		#print()
	return total

pics, numpics = doinput()
combos = findcombos(pics, numpics)
total = testcombos(combos)
print(int(total))


