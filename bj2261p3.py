# 분할정복을 처음부터 공부해보자

# (sorted, key, **를 배웠다)

#아이디어1
# 입력받은 좌표를 클래스로 저장하고 
# x축으로 정렬한 배열 y축으로 정렬한 배열을 하나씩 만들기
# 각각한번검색해서 x최소거리, y최소거리를 찾고
# 해당최소거리의 y거리, x거리를 구하고 그중 작은것을 기준으로 함
# 다시 그보다 작은 x,y거리를 모두 탐색후, 일괄 x^2+y^2 계산, 최소값 탐색

#문제점1
# mini가 0이 될 수 있는데 그러면 사실상 거의 모든 길이를 탐색해야함 (아마 시간초과가 걸릴듯)
# 반례: x축으로 x1-x2-x3가 놓여져 있을 때 x1-x3가 최단거리가 될 수 있음 (현재 알고리즘에서 고려x)
# 너무 날로 먹으려고 했다
# x최소거리에 대한 y최소거리를 다시 검색했어야 했음. 그래도 여전히 불완전하지만..

#아이디어1.1
# xmin과 ymin을 계산할 때 가로 세로를 모두 확인해서 보수적은 안전값을 잡았음
# mini = max(xmin,ymin); 임.
# 채점은 3%에서 막힌다. x와 y모두 인접하지 않은 상태에서도 최소값이 나올 수 있기 때문임.

#아이디어1.2
# 이렇게 얻은 안전값으로 바로 인접한 칸 뿐만 아니라 안전거리 내까지의 인덱스를 검색하기 (예 x1 - x2,x3,x4)
# 6프로까지감.

#아이디어 1.3
# 안전값의 sqrt(2) 배만큼 안전값을 확대
# 연산최적화를 위해 2배를 넣고 했는데 틀림
# 100배를 넣고해도 틀림. xmin = 10001을 해서 모든 경우의 수를 검사해야지만 시간초과가뜸.
# -> xmin을 구하는 과정에서 세로값과 비교할때 가로값은 x정렬이 되어있기에 반드시 양수지만 세로값은 음수가 될 수있는 문제점을 발견해서 abs함수를 사용해서 고쳤음. -> 똑같이 6프로
# -> xmin을 구하는 과정에서 부등호 잘못 들어간것 고침. xmin *= 2 ** 0.5 하고 다시 int로 형변환해서 구간검색을 최소화해서 최적화시킴. -> 8프로에서 시간초과

#아이디어 2
# xmin을 구하는 과정이 굉장히 단순한데 이것을 좀 더 복잡하게 해서 시간최적화시키기.
# xmin을 만족하는 유효한값을 만나면 이제 x^2+y^2 을 구해서 xmin을 갱신함
# 7% 20초에서 실패, 최소값을 구하는 코드가 누락되어있음. -> 고쳤으나 7% 20초

#아이디어 2.1
# ans를 구하기 전 가로, 세로값 모두 xmin과 비교를 한 후에 ans계산을 시작함 -> 8% 20초.. 아마 아주 약간의 성능 향상이 있었던 것 같다.

#아이디어 2.2
# xmin과 ymin은 이제 대충 훑어서 탐색한 가장 짧은 거리값이니까 이중 작은 값을 써도 무방함. mini = min(xmin, ymin) -> 8프로에서 시간초과 큰 이득은 없었다.

#아이디어 2.3
# xmin과 ymin을 완전히 mini로 통합하기. mini값을 구할 때 이웃한 칸이 아닌 칸도 조사할  수 있게하기 -> 밑에 내용을 그대로 수행하는게 아닌가? 머리가 잘 안돌아감

#아이디어 3
# 처음부터 ans와 mini = ans ** 0.5를 계속 줄여나가면서 문제 풀기 -> 6프로 틀림
# rtn이 너무 작은 문제 -> 해결함 -> 8프로 시간초과
# 근본적인 문제. 모든 점들의 간격이 1배 ~ 1.4배로 비슷하면, 즉 특수케이스가 없으면 거의 모든 경우의수를 정직하게 계산해야함.
# absum 변수로 tempX+tempY의 값이 최소선분길이의 루트2배, 45도가 될때 최대인점을 감안해서 이 이하로 들어올때만 계산을 하도록 최적화.

#아이디어 4
# 새로운 mini를 구할 때 마다 처음부터 시작(진행상황을 저장하기 어려움), 가로세로 2mini 만큼 쪼개서 진행. 2mini의 열벡터단위로 진행, 열벡터는 다시 2mini씩 세로로 쪼개짐.
# nextStart위치 잘 선정하기, 코드보수결과 10프로까지 도달했는데 틀림
# append에서 미리선언으로 바꿨는데 오히려 살짝 느려진듯.



import copy

class point:
    def __init__(self, coor):
        self.x = int(coor[0]);
        self.y = int(coor[1]);

"""
f = open("baekjoon/case2261_3.txt", "r");

n = int(f.readline());
po = [point([0, 0])] * n;
for i in range(0,n):
    po[i] = point(f.readline().split());
"""

n = int(input());
po = [point([0, 0])] * n;
for i in range(0,n):
    po[i] = point(input().split());



poX = sorted(po,key=lambda point: point.x);
#poY = sorted(po,key=lambda point: point.y);


rtn = (poX[1].x-poX[0].x) ** 2 + (poX[1].y - poX[0].y) ** 2;
mini = rtn ** 0.5 + 0.0001;
absum = mini ** 1.4143;


endFlag = 0;
resetFlag = 0;
nextStart = 0;
start = 0;

time = 0;

while (i < n):
    i = nextStart;
    m = 1;
    if (resetFlag == 0):
        i = 0;
    resetFlag = 1;
    nextFlag = 1;
    while (i + m < n and poX[i + m].x - poX[i].x < mini * 1.1):
        if (nextFlag and poX[i + m].x - poX[i].x > mini * 0.9):
            nextStart = i + m;
            nextFlag = 0;
        m += 1;
    section = [point([0, 0])] * m;
    for r in range(0, m):
        section[r] = poX[r + i];

    section = sorted(section, key=lambda point: point.y);
    j = 0;
    while (j < len(section) - 1 and resetFlag):
        k = 1;
        while(resetFlag):
            time += 1;
            tempY = section[j + k].y - section[j].y;
            if (tempY > mini):
                break;
            tempX = abs(section[j + k].x - section[j].x);
            if (tempX + tempY < absum):
                ans = (tempX ** 2 + tempY ** 2);
                if ans < rtn:
                    rtn = ans;
                    mini = rtn ** 0.5 + 0.0001;
                    absum = mini * 1.4143;
                    resetFlag = 0;
            k += 1;
            if (j + k == len(section)):
                break;
        j += 1;
    
    if nextFlag == 1 and resetFlag == 1:
        break;

print(rtn);
#print('time:',time);