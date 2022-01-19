n = int(input());

arr = [[0 for i in range(2)] for j in range(n)]

for i in range(0, n):
    arr[i][0], arr[i][1] = map(int, input().split());
    
arr.sort(key=lambda x : x[1]);
arr.sort(key=lambda x : x[0]);

for i in range(0,n):
    print(arr[i][0] , arr[i][1]);
