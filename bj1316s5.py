n = int(input());

rtn = 0;
for i in range(0,n):
    str = input();
    countFlag = 1;
    arr = [];
    arr.append(str[0]);
    for j in range(1,len(str)):
        if str[j] != str[j - 1]:
            for k in range(0, len(arr)):
                if arr[k] == str[j]:
                    countFlag = 0;
            arr.append(str[j]);
    rtn += countFlag;
print(rtn);
