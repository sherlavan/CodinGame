import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cry = {}
egg = {}
cells = {}
totalCry = 0

number_of_cells = int(input())  # amount of hexagonal cells in this map
for i in range(number_of_cells):
    # _type: 0 for empty, 1 for eggs, 2 for crystal
    # initial_resources: the initial amount of eggs/crystals on this cell
    # neigh_0: the index of the neighbouring cell for each direction
    _type, initial_resources, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    cells[i] = [0, 0, _type, initial_resources, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5]
    # cells[n][0] mark 
    if _type == 1:
        egg[i] = [initial_resources,99]
    if _type == 2:
        cry[i] = [initial_resources,99]
        totalCry+=initial_resources
    
# print(cells, file=sys.stderr, flush=True)
number_of_bases = int(input())
for i in input().split():
    my_base_index = int(i)
for i in input().split():
    opp_base_index = int(i)

def findclosesd(v,typ):
    que=[]
    mark = []
    que.append(v)
    dst = 0
    while que:
        point = que.pop(0)
        dst += 1
        for i in cells[point][4:]:
            if i>=0 and i not in mark:
                mark.append(i)
                if typ == "egg" and (i in egg) and i not in trace:

                    return i,dst
                    

                if typ == "eggsingle" and (i in egg):

                    return i,dst
                    

                if typ == "cry" and (i in cry) and i not in tracc:

                    return i,dst
                    

                if typ == "crysingle" and (i in egg):

                    return i,dst
                    

                if typ == "all" and (i in egg or i in cry) and i not in trac:

                    return i,dst
                    
                que.append(i)

    return -1,-1

q=[]
q.append(my_base_index)
print(cells, file=sys.stderr, flush=True)
while q:

    v = q.pop(0)
    cells[v][0] = 1
    dist = cells[v][1]
    for i in cells[v][4:]:
        if i >= 0 and cells[i][0] == 0:
            if cells[i][1]==0: cells[i][1]= dist + 1
            q.append(i)
            if cells[i][2]>0:
                if i in egg and egg[i][1]==99:
                    egg[i][1] = dist+1
                if i in cry and cry[i][1]==99:
                    cry[i][1] = dist+1



# game loop
while True:
    ma = 0
    oa = 0
    # print(cells, file=sys.stderr, flush=True)
    for i in range(number_of_cells):
        # resources: the current amount of eggs/crystals on this cell
        # my_ants: the amount of your ants on this cell
        # opp_ants: the amount of opponent ants on this cell
        resources, my_ants, opp_ants = [int(j) for j in input().split()]
        cells[i][3] = resources
        ma += my_ants
        oa += opp_ants
        if i in cry:
            if resources == 0:
                del cry[i]
            else:
                cry[i][0] = resources

        if i in egg:
            if resources == 0:
                del egg[i]
            else:
                egg[i][0] = resources

    # Write an action using print

    tracc={}
    lastp = my_base_index
    totaldist = 0
    
    for i in range(len(cry)):
        idx,d = findclosesd(lastp, "cry")
        totaldist+=d
        lastp = idx
        tracc[idx]=d
    
    trace={}
    lastp = my_base_index
    totaldist = 0
    
    for i in range(len(egg)):
        idx,d = findclosesd(lastp, "egg")
        totaldist+=d
        lastp = idx
        trace[idx]=d

    trac={}
    lastp = my_base_index
    totaldist = 0
    
    for i in range(len(egg)+len(cry)):
        idx,d = findclosesd(lastp, "all")
        totaldist+=d
        lastp = idx
        trac[idx]=d


    segg = dict(sorted(egg.items(), key=lambda x:x[1][1]))
    scry = dict(sorted(cry.items(), key=lambda x:x[1][1]))


    allp = scry | segg
    sall = dict(sorted(allp.items(), key=lambda x:x[1][1]))


    # WAIT | LINE <sourceIdx> <targetIdx> <strength> | BEACON <cellIdx> <strength> | MESSAGE <text>
    totaldist = 0
    p = 1
    lastp = my_base_index

               
    counter = 0
    for c in sall:
        if sall[c][1]<2 and totaldist < ma:
            counter+=1
            print(f"LINE {lastp} {c} {2};",end='')
            totaldist+=sall[c][1]

    for c in trac:
        if totaldist < ma and counter<4:
            print(f"LINE {lastp} {c} {1};",end='')
            totaldist+=trac[c]
            lastp = c
        
    if len(scry)<3:
        for c in scry:
            print(f"LINE {lastp} {c} {1};",end='')
            lastp = c 

    print("WAIT;")
