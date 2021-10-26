import math
n = int(input());
x = (1+(1+4*(n - 1)/3) ** 0.5) / 2;
if x % 1 > 0:
    print(int(x + 1));
else:
    print(int(x));