# 8*8 + 입력좌표에 대해 검사하는 기능 만들기

n, m = map(int, input().split());

arr = list();
for i in range(0, n):
    arr.append(input());
    
rtn2 = 64;
flag = 0;

for y0 in range(0, n - 8 + 1):
	for x0 in range(0, m - 8 + 1):
		rtn = 0;
		for y in range (0, 8):
			for x in range(0, 8):
				if arr[y0 + y][x0 + x] == 'W' and flag == 0:
					rtn += 1;
				elif arr[y0 + y][x0 + x] == 'B' and flag == 1:
					rtn += 1;
				flag = flag ^ 1;
			flag = flag ^ 1;
		rtn = min(rtn, 64 - rtn);
		rtn2 = min(rtn, rtn2);
print(rtn2);