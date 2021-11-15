n, m = map(int,input().split());

arr = list(map(int,input().split()));

sum = 0;

for i in range (0,len(arr)):
    for j in range(i + 1,len(arr)):
        for k in range(j + 1,len(arr)):
            tempsum = arr[i] + arr[j] + arr[k];
            if (tempsum > sum and tempsum <= m):
                sum = tempsum;
print(sum);