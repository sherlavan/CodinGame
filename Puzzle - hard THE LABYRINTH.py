import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]
print("init",r,c,a, file=sys.stderr)
karta = []
for j in range(r):
    karta.append([])
    for i in range(c):
        karta[j].append("?")

start = [-1, -1]
end = [-1, -1]
backpath = []

visitedpoints = []

counter = 0
flag = True
# game loop
while True:
    # kr: row where Kirk is located.
    # kc: column where Kirk is located.
    kr, kc = [int(i) for i in input().split()]
    visitedpoints.append([kr, kc])

    # print("now coords", kr, kc, file=sys.stderr)
    
    for i in range(r):
        row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        for j in range(len(row)):
            if row[j] =='?':
                continue
            elif row[j] =='#':
                karta[i][j] = math.inf
                continue
            if row[j] =='T':
                karta[i][j] = 0
                start = [j, i]
            if row[j] == '.' or row[j] =='T' or row[j] =='C':
                if karta[i][j] == '?':
                    karta[i][j] = -1
            if row[j] == 'C':
                end = [j, i]

        # print("map",row, file=sys.stderr)

    if flag:
        karta[kr][kc] = counter
        counter += 1

    if [kc, kr] == end:
        visitedpoints = []
        flag = False
        
        #reverse wave
        for st in karta:
            backpath.append([])
            for cell in st:
                if cell == '?':
                    backpath[-1].append(math.inf)
                    continue
                if cell == math.inf:
                    backpath[-1].append(math.inf)
                    continue
                # if cell == -1:
                #     backpath[-1].append(0)
                #     continue
                if cell < math.inf:
                    backpath[-1].append(0)
                    continue
                # backpath[-1].append(-1)        
        
        # print(backpath[kr], len(backpath), file=sys.stderr)
        backpath[start[1]][start[0]] = 1
        #  backpath[end[1]][end[0]], file=sys.stderr)
        # count pathback
        for step in range(1, a + 33):
            for i in range(len(backpath)):
                for j in range(len(backpath[i])):
                    if backpath[i][j] == step:
                            if backpath[i][j + 1] == 0:
                                backpath[i][j + 1] = step + 1

                            if backpath[i][j - 1] == 0:
                                backpath[i][j - 1] = step + 1

                            if backpath[i + 1][j] == 0:
                                backpath[i + 1][j] = step + 1

                            if backpath[i - 1][j] == 0:
                                backpath[i - 1][j] = step + 1
        # def wave(x, y):
        #     step = backpath[y][x]
        #     if backpath[y][x + 1] == 0:
        #         backpath[y][x + 1] = step + 1
        #         wave(x + 1, y)
            
        #     if backpath[y][x - 1] == 0:
        #         backpath[y][x - 1] = step + 1
        #         wave(x - 1, y)
            
        #     if backpath[y + 1][x] == 0:
        #         backpath[y + 1][x] = step + 1
        #         wave(x, y + 1)

        #     if backpath[y - 1][x] == 0:
        #         backpath[y - 1][x] = step + 1
        #         wave(x, y - 1)
        
        # wave(*start)
        # print(backpath[start[1]], file=sys.stderr)

    if not flag:
        karta = backpath.copy()
        for t in karta:
            print(t, file=sys.stderr)

    v = {} 

    if  [kr, kc + 1] not in visitedpoints:
        v.update({"RIGHT":karta[kr][kc + 1]})
    
    if [kr, kc - 1] not in visitedpoints:
        v.update({"LEFT":karta[kr][kc - 1]})

    if [kr + 1, kc] not in visitedpoints:
        v.update({"DOWN":karta[kr + 1][kc]})


    if [kr - 1, kc] not in visitedpoints:
        v.update({"UP":karta[kr - 1][kc]})

    if min(v.values()) == math.inf:
        visitedpoints = []
        v.update({"RIGHT":karta[kr][kc + 1]})
        v.update({"LEFT":karta[kr][kc - 1]})
        v.update({"DOWN":karta[kr + 1][kc]})
        v.update({"UP":karta[kr - 1][kc]})


    print(min(v.values()), v, file=sys.stderr)
    print(min(v, key = v.get))

    # Kirk's next move (UP DOWN LEFT or RIGHT).
    # print("RIGHT")
