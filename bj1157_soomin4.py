def check(value, banArr):
    for i in range (0, len(banArr)):
        for j in range (0, len(str(value))):
            if (int(str(value)[j]) == banArr[i]):
                return 1
    return 0


goal = int(input());
banNum = int(input());
banArr = list(map(int, input().split()))


upside = goal
while check(upside, banArr):
    upside += 1


downside = goal
while check(downside, banArr) and downside >= 0:
    downside -= 1

if (abs(goal - 100) <= abs(goal - upside) or abs(goal - 100) <= abs(goal - downside)):
    print(int(abs(goal - 100)))
elif (abs(goal - upside) >= abs(goal - downside)):
    print(int(abs(goal - downside)) + len(str(int(downside))))
else:
    print(int(abs(goal - upside)) + len(str(int(upside))))

exit (0)