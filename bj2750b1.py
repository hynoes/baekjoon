n = int(input());

arr = [];
for i in range(0,n):
    a = int(input());
    arr.append(a);

arr.sort();

for i in range(0,n):
    print(arr[i]);