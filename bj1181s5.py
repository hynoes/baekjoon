from logging import getLogRecordFactory


n = int(input());

arr = []

for i in range(0, n):
	a, b = input().split();

	a = int(a);
	
	temp = []
	temp.append(a);
	temp.append(b);
	arr.append(temp);
	
	
arr.sort(key=lambda x : x[0]);

for i in range(0,n):
	print(arr[i][0], arr[i][1])