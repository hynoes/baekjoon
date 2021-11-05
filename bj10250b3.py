t = int(input())

rtnArr = [];
for i in range(0,t):
    h, w, n = map(int, input().split())
    rtn = int(n / h + 0.9999);
    if n % h == 0:
        rtn += h * 100;
    else:
        rtn += (n % h)* 100;
    rtnArr.append(rtn);

for i in range (0,t):
    print(rtnArr[i]);