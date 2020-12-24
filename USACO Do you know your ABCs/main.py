#http://usaco.org/index.php?page=viewproblem2&cpid=1059
inp = input("")
#inp = "2 2 11 4 9 7 9"
nums = []
for i in range(7):
	nums.append(int(inp.split()[i]))
nums = sorted(nums)
def findABCs(nums):
	a = min(nums)
	tempnums = nums
	tempnums.remove(a)
	b = min(tempnums)
	c = max(nums)-b-a
	if a <= b <= c:
		return a,b,c
	elif a <= c <= b:
		return a,b,c
	elif b <= a <= c:
		return b,a,c
	elif b <= c <= a:
		return b,c,a
	elif c <= a <= b:
		return c,a,b
	elif c <= b <= a:
		return cba

a,b,c = findABCs(nums)
print(a,b,c)
