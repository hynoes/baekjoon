def rec(depth, n, arr, pick, min):
	if (depth == n / 2):
		pick1set = [0 for i in range(0, n)]
		for i in range(0, len(pick)):
			pick1set[pick[i]] = 1;
		pick2 = []
		for i in range(0, n):
			if pick1set[i] == 0:
				pick2.append(i)

		sum1 = 0;
		for i in range(0, len(pick)):
			for j in range(0, len(pick)):
				sum1 += arr[pick[i]][pick[j]];

		sum2 = 0;
		for i in range(0, len(pick2)):
			for j in range(0, len(pick2)):
				sum2 += arr[pick2[i]][pick2[j]];

		if (min[0] > abs(sum1 - sum2)):
			min[0] = abs(sum1 - sum2);
		return;
	for i in range(0, n):
		pick[depth] = i;
		flag = 0;
		for j in range(0, depth):
			if (pick[j] == i):
				flag = 1;
		if flag == 1:
			continue;
		rec(depth + 1, n, arr, pick, min);
		pick[depth] = -1;

n = int(input())

arr = []

for i in range(0, n):
	arr.append(list(map(int, input().split())))


pick = [-1 for i in range(int(n/2))];
min = [];
min.append(2099999999)
rec(0, n , arr, pick, min);

print(min[0]);