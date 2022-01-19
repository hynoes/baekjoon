n ,d = map(int,input().split());


n += 1;

while(1):
	if ((d - 1) ** (d - 1) >= n):
		n += 1;
		continue;
	if (d ** d < n):
		print(-1);
		break;
	arr = [];
	np = n;
	flag = 1;
	while (np != 0):
		arr.append(np % d);
		np = int(np / d);
	arr.sort();
	if (len(arr) != d):
		continue;
	for i in range(0,d):
		if (arr[i] != i):
			flag = 0;
	if (flag == 1):
		print(n);
		break;
	n += 1;
