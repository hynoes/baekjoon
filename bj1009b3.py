def myab(a, b):
    rtn = a;
    if (a == 0):
        return (10);
    for i in range (1,b):
        rtn *= a;
        rtn %= 10;
    return (rtn);

t = int(input());
arr = [0] * t;
for i in range (0,t):
    a, b = map(int,input().split());
    arr[i] = myab(a % 10,b);

for i in range (0, t):
    print(arr[i]);
