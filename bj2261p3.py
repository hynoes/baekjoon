#실패
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
# mini,rtn,absum이 갱신될 때 더 작은 mini를 가지고 현재의 i값에서 0부터 다시 시작하기 (x축 폭이 좁아져서 중복되는 연산이 소수 있더라도 제외하는 연산이 더 많을 확률이 훨씬 높아서 이득인듯)

#아이디어 4.1
# xmin,ymin을 구해서 mini로 사용하고 시작하기 -> 왠지 모르겠는데 계속 오류뜸

#아이디어 4.2
# 작은 rtn, mini값부터 시작하고 못찾으면 다시 올리기 -> 전체적인 루프는 많이 증가했지만, 일관된 속도를 얻을 수 있을것으로 기대 -> 11프로까지 빠르게 통과후 실패

#3가지 생략 아이디어. 
# 작은 mini, rtn값부터 올려가면서 작은해가 존재할 때 빠르게 찾기.
# 두점간의 거리가 mini보다 "크면" 수직한상황에서도 rtn값이 기존값보다 크므로 생략하기
# 이등변직각삼각형으로 제곱연산보다 빠르게 비교해서 제거하기 (면적이 아주 비슷하기 때문에 유용함)

#아이디어 4.3
# 2mini단위로 구간을 자를 때 마지막점뒤에 같은 x값을 가지는 점이 많을 경우 위험할 수 있는 생략이 됨 -> 그러한 점들을 모두 section에 추가함

#아이디어 5
# x가 같은 점이 몰리는 문제를 더 추가해서 해결하기 보다는, before Value~ beforeValue + 2 * mini 를 사용해서 poX를 section으로 분할하기
# mini가 갱신 될 경우도 유효함 (myrtn = 100 일 때 mymini 10보다 같거나 작은 모든 관계에 대해서 탐색했다면, 10이하의 답이 없다는 것이 보증되므로 )
# 구현하시오

#아이디어 5.1 (최적화)
# 이미 확인한 간격에 대해 추가로 확인 할 필요가 없는 최소치를 부여해서 연산을 아낌
# 하지만 구간탐색간격을 매번 크게 증가시키면 중복검색하는 점의 양이 전체에 비해 작은 양이므로 무시해도됨 (등비수열의합)
# 성능이 부족할 경우에만 추가로 구현하기
# myrtn 은 최초1로 제시 mymini = 1, myabsum = 1.4
# myrtn 을 n배한다면 ...

#아이디어 5.2
# 구간은 겹쳐져야함. 구간에 들어가지않는 인접한 점은 추가 할 필요가 없음!
# 2차원 section을 사용하기. 0<=x<=2n 이면 0 n<=x<=3n이면 1에 넣기 (핵심기술)

#아이디어 5.3
# 기존아이디어도 추가하기, areaSize는 정사각형범위를 의미하지만, 유효한 답을 찾을 경우
# 앞으로 추가적으로 탐색할 때 더 작은 areaSize를 찾을 수 있도록.
# 정사각형범위검색, 이미 탐색한 작은 정사각형에 대해 예외처리
# 논리적으로 작은 정사각형에 답이 있으면 큰 정사각형에 답이 필요 없으므로 작은 정사각형부터 탐색
# 그런데 어떻게 시간초과야 씨발롬아

#용어정리
# areaSize는 현재 검색에서 찾을 수 있는 가장 큰 선분길이
# beforeAreaSize는 0부터 값까지 검색완료가 보증된 값
# absum과 areaSize의 이등변삼각형, 정사각형차이는 그렇게 크지 않아보이므로 사용하지않음

#아이디어 5.4
# areaSize로 poX를 자를 때 반드시 areaSize로 엇박이 나야 하는데 만약에 중간에 areaSize를 갱신하면 그렇지 않게 된다.
# 새로운 areaSize를 발견하면 더이상 areaSize를 키우지 않고 남은 검색을 끝내고 종료하므로 오류가 발생할 위험이 있음.
# 해결법 -> odd와 even을 동시에 진행해야함
# 하지만 지금은 시간초과 해결이 우선이기에 적용하지 않음

#아이디어 5.5
# 탐색방법을 아이디어4로 다시 바꾸기




import copy
import sys

class point:
    def __init__(self, coor):
        self.x = int(coor[0]);
        self.y = int(coor[1]);


def search(section,endFlag,rtn,areaSize,absum):
    section = sorted(section,key=lambda point: point.y);
    for j in range(0,len(section) - 1):
        k = 0;
        while (1):
            k += 1;
            if (j + k == len(section)):
                break;
            tempY = section[j + k].y - section[j].y;
            if (tempY > areaSize):
                break;
            tempX = abs(section[j + k].x - section[j].x);
            # if (0 and tempX <= beforeAreaSize and tempY <= beforeAreaSize):
            #     continue;
            if tempX <= areaSize  and tempX + tempY < absum:
                ans = (tempX ** 2 + tempY ** 2);
                if ans < rtn:
                    rtn = ans;
                    if rtn ** 0.5 + 0.0001 < areaSize:
                        areaSize = rtn ** 0.5 + 0.0001;
                        absum = areaSize * 1.4143;
                    endFlag = 1;
    return endFlag, rtn, areaSize;




# f = open("baekjoon/case2261_4.txt", "r");
# n = int(f.readline());
# po = [point([0, 0])] * n;
# for i in range(0,n):
#     po[i] = point(f.readline().split());


n = int(input());
po = [point([0, 0])] * n;
for i in range(0,n):
    po[i] = point(input().split());



poX = sorted(po,key=lambda point: point.x);
poY = sorted(po,key=lambda point: point.y);

## --------------- 여기까지 입력 ----------------------

areaSize = 1;
beforeAreaSize = 0;
#global beforeAbsum;
#beforeAbsum = 0;

rtn = 100000000000000;
endFlag = 0;

while (endFlag == 0):
    areaSize *= 5;
    absum = areaSize * 1.4143;
    oddLimit = poX[0].x + areaSize;
    evenLimit = poX[0].x + areaSize * 2;
    section = [];
    for i in range(0,len(poX)):
        if (poX[i].x > oddLimit):
            endFlag, rtn, areaSize = search(section,endFlag,rtn,areaSize,absum);
            section = [];
            while (poX[i].x > oddLimit):
                oddLimit += areaSize * 2;
        section.append(poX[i]);
    endFlag, rtn, areaSize = search(section,endFlag,rtn,areaSize,absum);
    section = [];
    for i in range(0,len(poX)):
        if (poX[i].x > evenLimit):
            endFlag, rtn, areaSize = search(section,endFlag,rtn,areaSize,absum);
            section = [];
            while (poX[i].x > evenLimit):
                evenLimit += areaSize * 2;
        section.append(poX[i]);
    endFlag, rtn, areaSize = search(section,endFlag,rtn,areaSize,absum);
    section = [];
    beforeAreaSize = areaSize;
print(rtn);   


"""



#rtn = (poX[1].x-poX[0].x) ** 2 + (poX[1].y - poX[0].y) ** 2;
#mini = rtn ** 0.5 + 0.0001;
#absum = mini ** 1.4143;

i = 0;
while (i < n - 1):
    j = 1;
    while i + j < n and poX[i + j].x - poX[i].x == 0:
        if poX[i + j].y - poX[i].y == 0:
            print(0);
            quit();
        j += 1;
    i += j - 1;
    i += 1;
i = 0;
j = 0;




time1 = 0;
time2 = 0;
time3 = 0;
time4 = 0;
time5 = 0;


rtn = 1;
mini = 1;
absum = mini * 1.4143;

beforeValue = 0;

while (1):
    ansFlag = 0;
    i = 0;
    resetFlag = 1;
    nextStart = 0;
    while (beforeValue < poX[n - 1].x - poX[0].x):
        time1 += 1;
        
        if (resetFlag == 1): ## 리셋되지 않음
            i = nextStart;
        resetFlag = 1;
        # nextFlag = 1;
        # m = 1;
        # section = [];
        # if (i - 1 > 0):
        #     section.append(poX[i - 1]);
        # section.append(poX[i]);
        # while (i + m < n and poX[i + m].x - poX[i].x < mini * 2):
        #     if (nextFlag and poX[i + m].x - poX[i].x > mini * 1):
        #         nextStart = i + m;
        #         nextFlag = 0;
        #     section.append(poX[i + m]);
        #     m += 1;
        #     time2 += 1;
        # q = 0;
        # while (i + m + q < n and poX[i + m] == poX[i + m + q]):
        #     section.append(poX[i + m + q]);
        #     q += 1;
        while (poX[i + nextStart].x < beforeValue * mini):
            nextStart += 1;
        
        sectionCountIndex = 0;
        while (poX[i + sectionCountIndex].x < beforeValue + 2.01 * mini):
            section.append(poX[i + sectionCountIndex]);
            sectionCountIndex += 1;

        section = sorted(section, key=lambda point: point.y);
        j = 0;
        while (j < len(section) - 1 and resetFlag):
            k = 1;
            time3+= 1;
            while(resetFlag):
                time4 += 1;
                tempY = section[j + k].y - section[j].y;
                if (tempY > mini):
                    break;
                tempX = abs(section[j + k].x - section[j].x);
                if (tempX + tempY < absum):
                    time5 += 1;
                    ans = (tempX ** 2 + tempY ** 2);
                    if ans < rtn:
                        rtn = ans;
                        mini = rtn ** 0.5 + 0.0001;
                        absum = mini * 1.4143;
                        resetFlag = 0;
                        ansFlag = 1;
                        # print(rtn);
                        # print('time1:',time1);
                        # print('time2:',time2);
                        # print('time3:',time3);  
                        # print('time4:',time4);
                        # print('time5:',time5);
                    elif ans == rtn:
                        ansFlag = 1;
                k += 1;
                if (j + k == len(section)):
                    break;
            j += 1;
        
        if resetFlag == 1:
            break;
    if ansFlag == 1:
        break;
    else:
        rtn *= 100;
        mini *= 10;
        absum = mini * 1.4143;


print(rtn);
quit();
# print('time1:',time1);
# print('time2:',time2);
# print('time3:',time3);
# print('time4:',time4);
# print('time5:',time5);

"""