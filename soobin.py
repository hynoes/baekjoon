
goal = input();
banNum = int(input());
banArr = [0,0,0,0,0,0,0,0,0,0];

for i in range(0, banNum):
    temp = input();
    banArr[int(temp)] = temp;


i = 0;
upside = []
downside = []
while (i < len(goal) and goal[i] != banArr[int(goal[i])]):
    upside.append(goal[i])
    downside.append(goal[i])
    i += 1;
if (i <len(goal)):
    for j in range (int(goal[i]) + 1, 9):
        if 

while i < len(goal) :
    for j in range (0, 9):
        if banArr[j] == 0:
            downside.append(str(j))
            break;
    for k in range (9, 0, -1):
        if banArr[k] == 0:
            upside.append(str(k))
            break;
    i += 1;

downside = "".join(downside);
upside = "".join(upside);
print(upside);
print(downside);
