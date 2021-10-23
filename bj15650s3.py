def rec(arr, depth, m, n):
    if depth == n:
        for i in range(0,len(arr)):
            print(arr[i] + 1, end = ' ');
        return;
        
    for i in range(0, m):
        if depth == 0 or (depth > 0 and arr[depth - 1] < i):
            arr[depth] = i;
            rec(arr, depth + 1, m, n);
    return;

m, n = input().split();
m = int(m);
n = int(n);

arr = [0] * n;
rec(arr, 0, m, n);