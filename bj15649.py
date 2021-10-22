def btrk(arr,a,b,depth):
    if depth == b:
        for i in range(0,b):
            print(arr[i],end='');
            if i < b - 1:
                print(' ',end='');
        print("");
    else:
        for i in range(1,a + 1):
            flag = 0;
            for j in range(0,depth):
                if arr[j] == i:
                    flag = 1;
            if flag == 1:
                continue;
            arr[depth] = i;
            btrk(arr,a,b,depth + 1);
        

a, b = input().split();

a = int(a);
b = int(b);

arr = [0 for i in range(8)];
btrk(arr,a,b,0);