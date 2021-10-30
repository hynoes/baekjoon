import sys

n = int(sys.stdin.readline());

arr = [0] * n;
for i in range(0,n):
    arr[i] = int(sys.stdin.readline());

arr.sort();

for i in range(0,n):
    print(arr[i]);