x = int(input());

sum = 2;

a = 1;
b = 1;
time = 1;
if (time == x):
        print(b,'/',a);
        quit();
while (1):
    while(b != 1):
        a += 1;
        b -= 1;
        time += 1;
        if (time == x):
            print(b,'/',a);
            quit();
    a+=1;
    time += 1;
    if (time == x):
            print(b,'/',a);
            quit();
    while(a != 1):
        a -= 1;
        b += 1;
        time += 1;
        if (time == x):
            print(b,'/',a);
            quit();
    b+=1;
    time += 1;
    if (time == x):
            print(b,'/',a);
            quit();