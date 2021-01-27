
def spiral(arr,r,c):
	a = 0
	b = 0
	while a < r and b < c:
		for i in range(b, c):
			print(arr[a][i], end=' ')
		a += 1
		for i in range(a, r):
			print(arr[i][c-1],end=' ')
		c -= 1
		if a < r:
			for i in range(c-1, b-1, -1):
				print(arr[r -1][i], end=' ')
			r -= 1
		if b < c:
			for i in range(r-1, a-1, -1):
				print(arr[i][b],end =' ')
			b += 1	



arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
r = 3
c = 4
print(arr)
print()
spiral(arr, r, c)
