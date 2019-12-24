import sys
import numpy as np

"""
   目的地がありの時の最短経路検索
       src: それぞれの路線のノード番号を保持した配列
       dst: 目的地のノード番号
       dest: 目的地の有無
"""

"""
   待ち合わせ場所の解を返すメソッド
"""
def answer(route_map, nTown, src, dst, dest):
    num = len(src) #待ち合わせをする人数
    maindis = sys.maxsize #目的地までの最短距離
    mainvia = [0]*nTown #目的地までの経路情報を保持する
    infobox = [] #路線の使用人数と改札を保持した配列
    line = np.zeros(12)
    print("num "+str(num))

    kaisatu  = [[12,13],[14,15],[16],[17,18,19],[20,21],[22,23],[24,25,26,27,28,29,30,31,32,33],[25,34,35,36],[25,37,38],[40,41,42,44],[40,41,44],[40,41,44]]


    #路線が同じ人数を計算
    for n in range(num):
        line[src[n]] = line[src[n]] +1
    print("line: "+str(line))

    #各路線の人数と改札を保持した配列を作成
    dupl = 0 #重複人数
    for n in range(len(line)):
        if line[n]!=0:
            info = [line[n],kaisatu[n]]
            infobox.append(info)
    sort_infobox=sorted(infobox, key=lambda x:x[0], reverse=True)
    print(sort_infobox)
    print(sort_infobox[0][0])

    if dest: #目的地ありの時
        return Destination(route_map, nTown, sort_infobox, dst, len(sort_infobox))
    else: #目的地なしの時
        return noDestination(route_map, nTown, sort_infobox, len(sort_infobox))



"""
   目的地あり
"""
def Destination(route_map, nTown, src, dst, lineNum):
    maindis = sys.maxsize #目的地までの最短距離
    mainvia = [0]*nTown #目的地までの経路情報を保持する
    kaisatu = [sys.maxsize]*lineNum #各路線の改札保持
    mainline = sys.maxsize #メインルートの始点の路線
    meet = [] #合流方式、1地点方式の両方の待ち合わせの場所のノードを保持
    neardst = sys.maxsize #待ち合わせ場所の内dstへの最短距離
    nearmeet = sys.maxsize #待ち合わせ場所の内dstに最短の場所
    joinmeet = [] #合流方式で待ち合わせをするときの待ち合わせ場所を保持

    #メインルートを決定
    #路線重複ありの時
    if src[0][0]!=1: #重複があるとき
        if lineNum==1: #全員同路線
            for i in range(len(src[0][1])):
                d,v = solve(route_map, nTown, src[0][1][i], dst)
                if d<maindis:
                    maindis = d
                    M = src[0][1][i]
            kaisatu[0] = M
            meet.extend([[M],[M]])
            return (meet,kaisatu)
        if src[0][0]==src[1][0]==2:
            for n in range(lineNum):
                from_kaisatu_to_dst = sys.maxsize #改札からdstまでの最短距離保持(改札決定用)
                for i in range(len(src[n][1])):
                    d, v = solve(route_map, nTown, src[n][1][i], dst)
                    if d<from_kaisatu_to_dst:
                        from_kaisatu_to_dst = d
                        kaisatu[n] = src[n][1][i]
                        print(str(kaisatu[n])+"からの最短:　"+str(d))
                    if d<maindis:
                        maindis = d
                        for k in range(len(v)):
                            mainvia[k] = v[k]
                        mainline = n
            other=[] #メインルートの人以外の路線
            for l in range(lineNum):
                if l!=mainline:
                    other.append(kaisatu[l])
            print("")
            print("改札番号： "+str(kaisatu))
            print("目的地あり:　"+str(other))
            for i in range(len(other)):
                m,d = meetDist(route_map, nTown, other[i], dst, mainvia)
                joinmeet.append(m)
            for n in range(len(joinmeet)): #目的地に最も近い待ち合わせ場所を算出
                d,v = solve(route_map, nTown, joinmeet[n], dst)
                if d<neardst:
                    neardst = d
                    nearmeet = joinmeet[n]
            meet.extend([joinmeet,[nearmeet]])
            return (meet,kaisatu)

        #重複数に偏りがあるとき
        for n in range(lineNum):
            from_kaisatu_to_dst = sys.maxsize #改札からdstまでの最短距離保持(改札決定用)
            for i in range(len(src[n][1])):
                d, v = solve(route_map, nTown, src[n][1][i], dst)
                if d<from_kaisatu_to_dst:
                    from_kaisatu_to_dst = d
                    kaisatu[n] = src[n][1][i]
                    print(str(kaisatu[n])+"からの最短:　"+str(d))
                if n==0 and d<maindis:
                    maindis = d
                    for k in range(len(v)):
                        mainvia[k] = v[k]
                    mainline = n
        other=[] #メインルートの人以外の路線
        for l in range(lineNum):
            if l!=mainline:
                other.append(kaisatu[l])
        print("")
        print("改札番号： "+str(kaisatu))
        print("目的地あり:　"+str(other))
        for i in range(len(other)): #合流方式の待ち合わせ場所の算出
            m,d = meetDist(route_map, nTown, other[i], dst, mainvia)
            joinmeet.append(m)
        for n in range(len(joinmeet)): #目的地に最も近い待ち合わせ場所を算出
            d,v = solve(route_map, nTown, joinmeet[n], dst)
            if d<neardst:
                neardst = d
                nearmeet = joinmeet[n]
        meet.extend([joinmeet,[nearmeet]])
        return (meet,kaisatu)

    #路線重複なしの時(バラバラ)
    for n in range(lineNum):
        from_kaisatu_to_dst = sys.maxsize #各改札までの最短距離保持(改札決定のため)
        for i in range(len(src[n][1])):
            d, v = solve(route_map, nTown, src[n][1][i], dst)
            print(str(src[n][1][i])+"からの距離 : "+str(d))
            if d<from_kaisatu_to_dst: #各路線からの改札決定
                from_kaisatu_to_dst = d
                kaisatu[n] = src[n][1][i]
                print("min")
            if d<maindis: #最短距離のとき
                other=[] #メインルートの人以外の路線
                maindis = d
                for i in range(len(v)):
                    mainvia[i] = v[i]
                mainline = n
    for j in range(lineNum):
        if j!=mainline:
            other.append(kaisatu[j])
    print("")
    print("改札番号： "+str(kaisatu))
    print("目的地あり:　"+str(other))
    for i in range(len(other)):
        m,d = meetDist(route_map, nTown, other[i], dst, mainvia)
        joinmeet.append(m)
    for n in range(len(joinmeet)): #目的地に最も近い待ち合わせ場所を算出
        d,v = solve(route_map, nTown, joinmeet[n], dst)
        if d<neardst:
            neardst = d
            nearmeet = joinmeet[n]
    meet.extend([joinmeet,[nearmeet]])
    return (meet,kaisatu)



"""
   目的地なしの時
       src: 同じ路線を使用する人数と路線の改札を保持した配列
       num: 待ち合わせ人数
       lineNum: 使用路線数
"""
def noDestination(route_map, nTown, src, lineNum):
    maindis = sys.maxsize #目的地までの最短距離
    mainvia = [0]*nTown #目的地までの経路情報を保持する
    kaisatu = [] #各路線の改札保持
    goal = sys.maxsize #集まる所人のノード
    meet = [] #合流式、1地点式の両方の待ち合わせ場所を格納
    joinmeet = [] #合流式の待ち合わせ場所を格納
    onemeet = sys.maxsize #1地点(中間地点より)での待ち合わせ場所
    otherkaisatu = [] #出るべき改札を格納
    other_sumdis = 0 #メインルート以外の人の合流地点までの和(1地点待ち合わせ場所算出に利用)
    sumdis = sys.maxsize
    print("目的地なしの始点：　"+str(src))

    #重複時含む
    if src[0][0]!=1: #重複している
        if lineNum==1: #全員が同じ路線の時→改札を返す
            for i in range(len(src[0][1])):
                joinmeet.append(src[0][1][i])
                kaisatu.append(src[0][1][i])
            meet.extend([joinmeet,joinmeet])
            return (meet,kaisatu)
        if lineNum==2: #使用路線数が2→人数の多い路線の改札に集合するとき
            if src[0][0]==2 and src[1][0]==2: #4人.2.2
                for i in range(len(src[0][1])):
                    for j in range(len(src[1][1])):
                        d,v = solve(route_map, nTown,src[0][1][i],src[1][1][j])
                        if d<maindis:
                            maindis = d
                            start = src[0][1][i]
                            goal = src[1][1][j]
                            print("min")
                            for k in range(len(v)):
                                mainvia[k] = v[k]
                path = getPath(goal,mainvia)
                half = 0
                print("2人のpath:　"+str(path))
                for i in range(len(path)-1):
                    if half<maindis/2: #中間地点以下なら
                        half = half + route_map[path[i]][path[i+1]]
                        index = i+1
                print("distance: "+str(maindis)+" half: "+str(half))
                kaisatu.extend([start,goal])
                meet.extend([[path[index]],[path[index]]])
                return (meet,kaisatu)

            for i in range(len(src[0][1])):
                for j in range(len(src[1][1])):
                    d,v = solve(route_map, nTown, src[0][1][i], src[1][1][j])
                    print("改札"+str(src[0][1][i])+"から"+str(src[1][1][j])+"の距離： "+str(d))
                    print("改札"+str(src[0][1][i])+"から"+str(src[1][1][j])+"までの経路:　"+str(getPath(src[1][1][j],v)))
                    if d<maindis: #メインルートなら
                        start = src[0][1][i]
                        goal = src[1][1][j]
                        maindis = d
                        M = src[0][1][i]
            kaisatu.extend([start,goal])
            meet.extend([[M],[M]])
            return (meet,kaisatu)

        #以降使用路線数が2以上の時
        if src[0][0]==src[1][0]==2: #5人.2.2.1
            for n in range(lineNum-1):
                for i in range(len(src[n][1])):
                    for j in range(len(src[n+1][1])):
                        d,v = solve(route_map, nTown, src[n][1][i], src[n+1][1][j])
                        if d<maindis:
                            maindis = d
                            other=[] #メインルートの人以外の路線
                            goal = src[n+1][1][j] #メインルートの終点
                            start = src[n][1][i] #メインルートの始点(デバック用)
                            print("min")
                            for k in range(len(v)):
                                mainvia[k] = v[k]
                            for l in range(lineNum):
                                if l!=n and l!=n+1:
                                    other.append(src[l][1])

        else:
            for n in range(len(src)-1):
                for i in range(len(src[0][1])): #最大路線重複数
                    for j in range(len(src[n+1][1])):
                        d,v = solve(route_map, nTown, src[0][1][i], src[n+1][1][j])
                        print("改札"+str(src[0][1][i])+"から"+str(src[n+1][1][j])+"の距離： "+str(d))
                        print("改札"+str(src[0][1][i])+"から"+str(src[n+1][1][j])+"までの経路:　"+str(getPath(src[n+1][1][j],v)))
                        if d<maindis:
                            other=[] #メインルートの人以外の路線
                            goal = src[n+1][1][j] #メインルートの終点
                            start = src[0][1][i] #メインルートの始点(デバック用)
                            maindis = d
                            print("min")
                            for k in range(len(v)):
                                mainvia[k] = v[k]
                            for l in range(lineNum):
                                if l!=0 and l!=n+1:
                                    other.append(src[l][1])

        print("目的地なしのother：　"+str(other))
        print("mainstart: "+str(start))
        print("maingoal: "+str(goal))
        #メインルート以外の人が合流する地点を算出
        for n in range(len(other)):
            mindis = sys.maxsize #otherそれぞれのmeetへの最短距離
            for i in range(len(other[n])):
                m,d = meetDist(route_map, nTown, other[n][i], goal, mainvia)
                if d<mindis:
                    mindis = d
                    M = m
                    kai = other[n][i] #otherからmeetに行くときの最短の改札
            otherkaisatu.append(kai)
            joinmeet.append(M)
        #合流地点(joinmeet)の内otherの距離の差が小さいほう
        for m in range(len(joinmeet)):
            for i in range(len(otherkaisatu)):
                d,v = solve(route_map, nTown, otherkaisatu[i], joinmeet[m])
                other_sumdis = other_sumdis+d
            if other_sumdis<sumdis:
                onemeet = joinmeet[m]

        kaisatu.extend([start,goal])
        for i in range(len(otherkaisatu)):
            kaisatu.append(otherkaisatu[i])
        meet.extend([joinmeet,[onemeet]])
        print("改札番号：　"+str(start)+","+str(goal)+","+str(otherkaisatu))
        return (meet,kaisatu)

    #路線重複がないとき(バラバラ)
    for n in range(lineNum):
        stationdis = sys.maxsize #駅から改札までの最短距離を保持
        print(str(n+1)+"人目の改札：　"+str(src[n][1]))
        for i in range(len(src[n][1])):
            if (lineNum-1-n)!=0:
                for m in range((lineNum-1-n)):
                    for j in range(len(src[m+n+1][1])):
                        d,v = solve(route_map, nTown, src[n][1][i], src[m+n+1][1][j])
                        print("改札"+str(src[n][1][i])+"から"+str(src[m+n+1][1][j])+"の距離： "+str(d))
                        print("改札"+str(src[n][1][i])+"から"+str(src[m+n+1][1][j])+"までの経路:　"+str(getPath(src[m+n+1][1][j],v)))
                        if d<maindis:
                            other=[] #メインルートの人以外の路線
                            goal = src[m+n+1][1][j] #メインルートの終点
                            start = src[n][1][i] #メインルートの始点(デバック用)
                            maindis = d
                            print("min")
                            for k in range(len(v)):
                                mainvia[k] = v[k]
                            for l in range(lineNum):
                                if l!=(m+n+1) and l!=n:
                                    other.append(src[l][1])
    print("目的地なしのother：　"+str(other))
    print("mainstart: "+str(start))
    print("maingoal: "+str(goal))
    kaisatu.extend([start,goal])
    if lineNum==2:
        path = getPath(goal,mainvia)
        half = 0
        print("2人のpath:　"+str(path))
        for i in range(len(path)-1):
            if half<maindis/2: #中間地点以下なら
                half = half + route_map[path[i]][path[i+1]]
                index = i+1
        print("distance: "+str(maindis)+" half: "+str(half))
        meet.append(path[index])
        return (meet,kaisatu)
    for n in range(len(other)):
        mindis = sys.maxsize #otherそれぞれのmeetへの最短距離
        for i in range(len(other[n])):
            m,d = meetDist(route_map, nTown, other[n][i], goal, mainvia)
            if d<mindis:
                mindis = d
                M = m
                kai = other[n][i] #otherからmeetに行くときの最短の改札
        otherkaisatu.append(kai)
        joinmeet.append(M)
    #合流地点(joinmeet)の内otherの距離の差が小さいほう
    for m in range(len(joinmeet)):
        for i in range(len(otherkaisatu)):
            d,v = solve(route_map, nTown, otherkaisatu[i], joinmeet[m])
            other_sumdis = other_sumdis+d
        if other_sumdis<sumdis:
            onemeet = joinmeet[m]
    for i in range(len(otherkaisatu)):
        kaisatu.append(otherkaisatu[i])
    meet.extend([joinmeet,[onemeet]])
    print("改札番号：　"+str(start)+","+str(goal)+","+str(otherkaisatu))
    return (meet,kaisatu)


"""
   目的地ありの時
   最短距離で出会うノードを探索するメソッド
      src: スタート地点
      dst: 目的地
      via: メインルートの経路
"""
def meetDist(route_map, nTown, src, dst, via):
    MEET = sys.maxsize #待ち合わせ場所の初期値
    mainroute = getPath(dst,via) #メインルート
    print("mainroute: "+str(mainroute))
    dist = sys.maxsize #メインルートへの最短距離
    for i in range(len(mainroute)):
        d, v = solve(route_map, nTown, src, mainroute[i])
        if d<dist:
            dist = d
            MEET = mainroute[i]
    print(str(src)+"からmeetまでのdist: "+str(dist))
    return (MEET,dist)

"""
   最短経路探索を行うメソッド
      src: スタート地点
      dst: ゴール
"""
def solve(route_map, nTown, src, dst):
    #初期化
    #最短距離の初期値は無限遠
    distance = np.array([sys.maxsize]*nTown) #各都市の最短距離
    fixed = [False]*nTown #最短距離が確定していない
    via = [-1]*nTown #その都市へ最短経路で到達する直前の都市
    distance[src] = 0 #出発地点までの距離を0とする

    #未確定の中での最も近い都市を求める
    while True:
        marked = minIndex(distance, fixed, nTown)
        if marked<0: #全都市が確定した場合
            return(sys.maxsize,via)
        if distance[marked]==sys.maxsize: #非連結グラフ→つながっていないと無限大のまま
            return(distance[marked],via)
        fixed[marked] = True #その都市までの最短距離は確定
        if marked==dst: #目的地までの距離が確定したので終了
            return(distance[dst], via)
        for j in range(nTown): #隣の都市(i)について
            if route_map[marked][j]>0 and fixed[j]==False: #まだ未確定
                #markedが表す都市を経由した距離求める
                newDistance = distance[marked]+route_map[marked][j]
                #meaked経由の距離が今までよりも小さければ更新する
                if newDistance<distance[j]:
                    distance[j] = newDistance
                    via[j] = marked #直前の都市を記憶


"""
   まだ最短距離が確定していない都市の中で、最も近いものを探すメソッド
"""
def minIndex(distance, fixed, nTown):
    dist = sys.maxsize#最短距離の初期値
    idx = -1#都市のIDの初期値
    for i in range(nTown):
        if fixed[i]==False and distance[i]<dist:#未確定で距離が小さい都市
            dist = distance[i]
            idx = i
    return idx


"""
   最短経路までの道のりを記録する
"""
def getPath(dst, via): #srcからdstまでの経路を返す
    #srcからdstまでの経路を配列にして返す
    #dstからsrcまでの経路をたどってArrayListを作る
    x = dst
    array = [] #Listを作成
    while x > -1: #via[x]=-1 なら始点に戻るまで続ける
        array.append(x) #xを記録
        x = via[x]
    route = [0]*len(array) #最終的な経路を記録する配列
    #arrayの逆順をrouteに記録して返す
    for i in range(len(route)):
        route[i] = array[len(array)-1-i]
    return route
