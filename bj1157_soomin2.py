import math

def minus(value, scale, banArr, goal):
    banFlag = 1
    while (banFlag == 1 and value >= scale):
        banFlag = 0
        value -= scale
        for i in range (0, 10):
            for j in range (0, len(str(value)) - int(math.log10(scale))):
                if (str(value)[j] == banArr[i]):
                    banFlag = 1
    return value

def plus(value, scale, banArr, goal):
    banFlag = 1
    while (banFlag == 1 and value <= scale):
        banFlag = 0
        value += scale
        for i in range (0, 10):
            for j in range (0, len(str(value)) - int(math.log10(scale))):
                if (str(value)[j] == banArr[i]):
                    banFlag = 1
    return value



goal = int(input());
banNum = int(input());
banArr = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

for i in range(0, banNum):
    temp = input();
    banArr[int(temp)] = temp;


i = 0;
scale = pow(10,len(str(goal)) - 1)
upside = scale * 10;
while scale >= 1 :
    if (minus(upside, scale, banArr, goal) > goal):
        upside = minus(upside, scale, banArr, goal)
    else:
        scale /= 10

scale = pow(10,len(str(goal)) - 1)
downside = 0
while scale >= 1 :
    if (plus(downside, scale, banArr, goal) < goal):
        downside = plus(downside, scale, banArr, goal)
    else:
        scale /= 10

if (abs(goal - upside) >= abs(goal - downside)):
    print(int(goal - downside) + len(str(int(downside))))
else:
    print(int(goal - upside) + len(str(int(upside))))
