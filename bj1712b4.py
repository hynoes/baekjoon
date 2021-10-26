import math

a, b ,c = input().split();
a = int(a);
b = int(b);
c = int(c);

if (b >= c):
    print(-1);
    quit();

ans = (a/(c-b));
if (ans % 1 == 0):
    ans += 1;
else:
    ans = math.ceil(ans);
print(int(ans));