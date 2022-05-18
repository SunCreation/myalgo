problem = (10,10,[[10,15,4,3,4],[20,20,2,2,1]])

def solution(alp, cop, problems):
    problemcontent = ['alre','core','alrw','corw','cost']
    cantlist = list(range(len(problems)))
    prodict = {}
    for content in zip(problemcontent,zip(*problems)):
        # print(content)
        prodict[content[0]] = content[1:][0]
    # print(prodict)
    # 목표점수를 정한다.
    # g_al = max(prodict['alre'])
    # g_co = max(prodict['core'])
    # 지금 정해놓지 않고 필요할 때 정해서 사용한다.
    print(prodict)
    learntime = 0
    point = [alp, cop, learntime]
    solvelist = set()
    prodict['ratio'] = []


    for i, problem in enumerate(problems):
        if alp > problem[0] and cop > problem[1]: solvelist.add(i)
        prodict['ratio'].append((problem[2]/problem[4], problem[3]/problem[4], problem[4]))

    def check_solve():
        for i, problem in enumerate(problems):
            if point[0] > problem[0] and point[1] > problem[1]: solvelist.add(i)

    def learn_al():
        point[0] += 1
        point[2] += 1

    def learn_co():
        point[1] += 1
        point[2] += 1

    def solvepro(num):
        point[0] += prodict['alrw'][num]
        point[1] += prodict['corw'][num]
        point[2] += prodict['cost'][num]

    def check_upper(num):
        g_al, g_co, _,_,_ = [pr for i, pr in enumerate(problems) if i not in solvelist]
        alre = max(g_al - point[0],0)
        core = max(g_co - point[1],0)
        score = alre
        selection = -2
        comparelist = []
        for i in solvelist:
            aratio, cratio, cost = prodict['ratio'][i]
            if score < (alre * aratio + core * cratio):
                score = alre * aratio + core * cratio
                selection = i
        if score < core:
            selection = -1
        return selection
    
    def proposecheck():
        ...

    # upperlist = [learn_al, learn_co, solvepro]

    while point[0] < g_al or point[1] < g_co:
        idx = check_upper()
        print(idx, point[0],point[1], point[2])
        if idx==-2: learn_al()
        elif idx==-1: learn_co()
        else: solvepro(idx)
        check_solve()

    return point[2]

print(solution(*problem))