def dupcheck(temp):
	for i in range(0, 9):
		for j in range(i +1, 9):
			if (temp[i] != 0 and temp[j] != 0 and temp[i] == temp[j]):
				return 1
	return 0

def check(arr, m, n):
	for j in range(0,9):
		if (j == n):
			continue
		if (arr[m][n] == arr[m][j]):
			return 1

	for j in range(0,9):
		if (j == m):
			continue
		if (arr[m][n] == arr[j][n]):
			return 1

	for j in range (0,9):
		m1 = 3 * int(m / 3) + int(j / 3)
		n1 = 3 * int(n / 3) + j % 3
		if (m == m1 and n == m1):
			continue
		if (arr[m][n] == arr[m1][n1]):
			return 1

	return 0

def check0(arr):
	for i in range(8,-1,-1):
		for j in range(8,-1,-1):
			if (arr[i][j] == 0):
				return 1
	return 0
		

def rec(arr, arr0, index, max):
	if(index == max):
		end(arr)
	i = arr0[index][0]
	j = arr0[index][1]
	for k in range(1,10):
		arr[i][j] = k
		if (check(arr,i,j) == 0):
			rec(arr, arr0, index + 1, max)
	arr[i][j] = 0
       
def end(arr):
	for i in range(0,9):
		for j in range(0,9):
			print(arr[i][j], end = ' ')
		print()
	quit()


arr = []
for i in range (0, 9):
	temp = list(map(int, input().split()))
	arr.append(temp)
 
arr0 = []
count = 0
for i in range(0,9):
	for j in range(0,9):
		if (arr[i][j] == 0):
			count += 1
			temp = []
			temp.append(i)
			temp.append(j)
			arr0.append(temp)
    

rec(arr, arr0, 0, count)
 
