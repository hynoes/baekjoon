n = int(input());
i = 666;
count = 0;
while(1):
	len1 = len(str(i));
	temp = 0;
	max1 = 0;
	for j in range(0, len1):
		if (str(i)[j] == '6'):
			temp += 1;
		else:
			temp = 0;
		max1 = max(temp,max1);
	if max1 >= 3:
		count += 1;
	if n == count:
		print(i);
		break;
	i += 1;