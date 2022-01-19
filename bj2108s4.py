n = int(input())

arr = []
for i in range(0,n):
	arr.append(int(input()))
    
arr.sort()

avg= round(sum(arr)/n)
print(avg)

print(arr[int(n/2)])

most = []
mostcount = 0

count = 0

for i in range(0,n):
	if (i > 0 and arr[i - 1] != arr[i]):
		if (count == mostcount):
			most.append(arr[i - 1])
		elif (count > mostcount):
			most = []
			most.append(arr[i - 1])
			mostcount = count
		count = 0
	elif (i == len(arr) - 1):
		count += 1
		if (count == mostcount):
			most.append(arr[i])
		elif (count > mostcount):
			most = []
			most.append(arr[i])
			mostcount = count
	count += 1

most.sort()
if (len(most) > 1):
	print(most[1])
else:
	print(most[0])
 
print(max(arr) - min(arr))