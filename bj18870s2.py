# dictionary의 필요성과 key를 통해 value를 얻기
# https://wikidocs.net/16

n = int(input());
arr = list(map(int, input().split()));
arr2 = arr.copy();

setarr= set(arr);
arr = list(setarr);
arr.sort(key=lambda x: x);

dict = {}

for i in range(0, len(arr)):
    dict[arr[i]] = i;
        

for i in range(0, n):
    print(dict[arr2[i]], end = ' ');
