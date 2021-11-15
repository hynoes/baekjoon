t = int(input());
rtn = [];
    

for i in range(0,t):
    arr = [];
    arr = list(map(int,input().split()));
    if (arr[2] > arr[5]):
        arr[0] , arr[3] = arr[3], arr[0];
        arr[1] , arr[4] = arr[4], arr[1];
        arr[2] , arr[5] = arr[5], arr[2];
    dist1 = (arr[0] - arr[3]) ** 2 + (arr[1] - arr[4]) ** 2;
    dist2 = (arr[2] + arr[5])**2;
    if (arr[0] == arr[3] and arr[1] == arr[4]):
            if (arr[2] == arr[5]):
                rtn.append(-1);
            else:
                rtn.append(0);
    elif dist1 <= arr[5] ** 2:
        if dist1   < (arr[5] - arr[2]) ** 2:
            rtn.append(0);
        elif dist1  == (arr[5] - arr[2]) ** 2:
            rtn.append(1);
        else:
            rtn.append(2);
    else:
        if (dist1 > dist2):
            rtn.append(0);
        elif (dist1 < dist2):
            rtn.append(2);
        else:
            rtn.append(1);        

for i in range(0,t):
    print(rtn[i]);
    