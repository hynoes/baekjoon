def findsolo(arr):
    for i in range (0, len(arr)):
        meetcount = 0;
        for j in range (0, len(arr)):
            if (arr[i] == arr[j]):
                meetcount += 1;
        if meetcount == 1:
            return (arr[i]);
        
        
arrX = [];
arrY = [];
for i in range (0,3):
    x , y = map(int, input().split());
    arrX.append(x);
    arrY.append(y);
    
print(findsolo(arrX), findsolo(arrY));