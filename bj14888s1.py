def rec(depth, value, arr, oper, minmax):
	if (depth == len(arr)):
		if (value < minmax[0]):
			minmax[0] = value;
		if (value > minmax[1]):
			minmax[1] = value;
		return;
	value0 = value;
	if (oper[0] > 0):
		value += arr[depth];
		oper[0] -= 1;
		rec(depth + 1, value, arr, oper, minmax);
		oper[0] += 1;
		value = value0;
	if (oper[1] > 0):
		value -= arr[depth];
		oper[1] -= 1;
		rec(depth + 1, value, arr, oper, minmax);
		oper[1] += 1;
		value = value0;
	if (oper[2] > 0):
		value *= arr[depth];
		oper[2] -= 1;
		rec(depth + 1, value, arr, oper, minmax);
		oper[2] += 1;
		value = value0;
	if (oper[3] > 0):
		value = int(value / arr[depth]);
		oper[3] -= 1;
		rec(depth + 1, value, arr, oper, minmax);
		oper[3] += 1;
		value = value0;

  
  
  

n = int(input())

arr = list(map(int,input().split()))

oper = list(map(int,input().split()))

minmax = []
minmax.append(1000000001);
minmax.append(-1000000001);
rec(1, arr[0], arr, oper, minmax);
print(minmax[1])
print(minmax[0])


