n = int(input());

for i in range (0, 10):
    if n % 5 == 0:
        print(int(n/5 + i));
        quit();
    elif n < 0:
        print(-1);
        quit();
    n -= 3;
print(-1);