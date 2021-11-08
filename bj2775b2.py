t = int(input());
rtn = [];

for i in range (0,t):
    k = int(input());
    n = int(input());
    arr = [];
    arr = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12 ,13, 14]];
    for j in range (1,k):
        arr.append([0]*14);
        for m in range (0, n):
            arr[j][m] = 0;
            for o in range (0, m + 1):
                arr[j][m] += arr[j - 1][o];
    sum = 0;
    for j in range (0, n):
        sum += arr[k - 1][j];
    rtn.append(sum);
for i in range (0,t):
    print(rtn[i]);
