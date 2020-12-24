#https://train.usaco.org/usacoprob2?a=fxKXvyWsW9y&S=beads
"""
ID: tobyewo1
LANG: PYTHON3
TASK: beads
"""
with open("beads.in", "r") as f:
	theInput = f.readlines()
length = int(theInput[0])
necklace = theInput[1].strip()
  

def findValue(length, necklace):
	results = []
	for iteration in range(length):
		streak_clockwise_color = necklace[iteration]
		streak_counterclockwise_color = necklace[iteration-1]
		streak_clockwise = 0
		streak_counterclockwise = 0
		iterator = 0

		print("Current bead color is " + str(necklace[iteration+iterator]))

		if streak_clockwise_color == 'w':
			streak_clockwise_r = 0
			streak_clockwise_b = 0
			streak_clockwise_color = 'b'
			while necklace[(iterator+iteration)%length] == streak_clockwise_color or necklace[(iterator+iteration)%length] == 'w':
				streak_clockwise_b += 1
				iterator += 1
				if iterator > length:
					return length
			streak_clockwise_color = 'r'
			while necklace[(iterator+iteration)%length] == streak_clockwise_color or necklace[(iterator+iteration)%length] == 'w':
				streak_clockwise_r += 1
				iterator += 1
				if iterator > length:
					return length
				
			streak_clockwise = max(streak_clockwise_r, streak_clockwise_b)
		else:
			while necklace[(iterator+iteration)%length] == streak_clockwise_color or necklace[(iterator+iteration)%length] == 'w':
				streak_clockwise += 1
				iterator += 1
		
				if iterator > length:
					return length

		iterator = 0

		if streak_counterclockwise_color == 'w':
			streak_counterclockwise_r = 0
			streak_counterclockwise_b = 0
			streak_counterclockwise_color = 'b'
			while necklace[(iterator+iteration)] == streak_counterclockwise_color or necklace[(iterator+iteration)] == 'w':
				print("At iterator " + str(iterator) + " at iteration " + str(iteration) + " we have color " + str(necklace[(iterator+iteration)]))
				print("in loop b")
				streak_counterclockwise_b += 1
				iterator -= 1
			streak_counterclockwise_color = 'r'
			while necklace[(iterator+iteration)] == streak_counterclockwise_color or necklace[(iterator+iteration)] == 'w':
				print("At iterator " + str(iterator) + " at iteration " + str(iteration) + " we have color " + str(necklace[(iterator+iteration)]))
				print("in loop r")
				streak_counterclockwise_r += 1
				iterator -= 1
			streak_counterclockwise = max(streak_counterclockwise_r, streak_counterclockwise_b)
		else:
			while necklace[(iterator+iteration)] == streak_counterclockwise_color or necklace[(iterator+iteration)] == 'w':
				streak_counterclockwise += 1
				iterator -= 1


		print(str(iteration) + " " + str(streak_clockwise + streak_counterclockwise))
		results.append(streak_clockwise + streak_counterclockwise)
		
	return max(results)
with open("beads.out", "w+") as f:
		f.write(str(findValue(length, necklace)))
			

			
