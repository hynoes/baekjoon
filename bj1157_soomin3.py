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

def check(value, banArr, goal):
    for i in range (0, 10):
        for j in range (0, len(str(value))):
            if (str(value)[j] == banArr[i]):
                return 1
    return 0


goal = int(input());
banNum = int(input());
banArr = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

for i in range(0, banNum):
    temp = input();
    banArr[int(temp)] = temp;


i = 0;
scale = pow(10,len(str(goal)) - 1)
upside = scale * 10;
while upside >= goal:
    if (check(upside - 1, banArr, goal) == 0):
        upside -= 1
        upsideTrue = upside
    else:
        upside -= 1


downside = 0
while downside <= goal:
    if (check(downside + 1, banArr, goal) == 0):
        downside += 1
        downsideTrue = downside
    else:
        downside += 1

if (abs(goal - upsideTrue) >= abs(goal - downsideTrue)):
    print(int(goal - downsideTrue) + len(str(int(downsideTrue))))
else:
    print(int(goal - upsideTrue) + len(str(int(upsideTrue))))
