def checker(arr, i):
    if (i >= len(arr)):
        return (-1);
    if (i < len(arr) and arr[i] == 'c'):
        if (i + 1 < len(arr) and (arr[i + 1] == '=' or arr[i + 1] == '-')):
            return(i + 2);
    if (i < len(arr) and arr[i] == 'd'):
        if (i + 1 < len(arr) and arr[i + 1] == 'z'):
            if (i + 2 < len(arr) and arr[i + 2] == '='):
                return(i + 3);
        if (i + 1 < len(arr) and arr[i + 1] == '-'):
            return(i + 2);
    if (i + 1 < len(arr)):
        if (arr[i] == 'l' and arr[i+1] == 'j'):
            return(i + 2);
        if (arr[i] == 'n' and arr[i+1] == 'j'):
            return(i + 2);
        if (arr[i] == 's' and arr[i+1] == '='):
            return(i + 2);
        if (arr[i] == 'z' and arr[i+1] == '='):
            return(i + 2);
    return (i + 1);
    
        

str = input();

i = 0;
count = 0;
while (i != -1):
    i = checker(str, i);
    count += 1;
print(count - 1);