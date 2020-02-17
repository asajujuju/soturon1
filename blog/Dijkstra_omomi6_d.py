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
    for n in src:
        line[n] = line[n] +1
    print("line: "+str(line))

    #各路線の人数と改札を保持した配列を作成
    dupl = 0 #重複人数
    for n in range(len(line)):
        if line[n]!=0:
            infobox.extend([[line[n],kaisatu[n]]])
    print("infobox: "+str(infobox))
    sort_infobox=sorted(infobox, key=lambda x:x[0], reverse=True)

    if dest: #目的地ありの時
        return Destination(route_map, nTown, sort_infobox, dst, len(sort_infobox))
    else: #目的地なしの時
        return noDestination(route_map, nTown, sort_infobox, len(sort_infobox))



"""
   目的地あり
"""
def Destination(route_map, nTown, src, dst, lineNum):
    maindis = sys.maxsize #目的地までの最短距離
    kaisatu = [sys.maxsize]*lineNum #各路線の改札保持
    mainline = sys.maxsize #メインルートの始点の路線
    meet = [] #1地点の待ち合わせの場所のノードを保持
    neardst = sys.maxsize #待ち合わせ場所の内dstへの最短距離
    nearmeet = sys.maxsize #待ち合わせ場所の内dstに最短の場所
    nearpathlist = [] #nearmeetに行くための経路のリスト
    srcdist = np.zeros(lineNum) #各路線利用者の目的地までの最短距離

    #メインルートを決定
    #路線重複ありの時
    if src[0][0]!=1: #重複があるとき
        if lineNum==1: #全員同路線
            for i in src[0][1]:
                d,v = solve(route_map, nTown, i, dst)
                if d<maindis:
                    maindis = d
                    M = i
                    via = v
            kaisatu[0] = M
            nearpathlist.append(getPath(dst,via))
            print("nearpathlist : "+str(nearpathlist))
            meet.append(M)
            return (meet,kaisatu,nearpathlist)
        if src[0][0]==src[1][0]==2:
            for n in range(lineNum):
                from_kaisatu_to_dst = sys.maxsize #改札からdstまでの最短距離保持(改札決定用)
                for i in src[n][1]:
                    d, v = solve(route_map, nTown, i, dst)
                    if d<from_kaisatu_to_dst:
                        from_kaisatu_to_dst = d
                        kaisatu[n] = i
                        print(str(kaisatu[n])+"からの最短:　"+str(d))
                    if d<maindis:
                        maindis = d
                        mainvia = v
                        mainline = n
                srcdist[n] = maindis
            nearpathlist.append(getPath(dst,mainvia))
            print("")
            print("改札番号： "+str(kaisatu))
            for n in range(lineNum):
                if n!=mainline:
                    m,d = meetDist(route_map, nTown, kaisatu[n], dst, mainvia)
                    to_dst = srcdist[n]-d
                    if to_dst<neardst:
                        neardst = to_dst
                        nearmeet = m
            for n in range(lineNum):
                if n!=mainline:
                    d,v = solve(route_map, nTown, kaisatu[n], nearmeet)
                    nearpathlist.append(getPath(nearmeet,v))
            print("nearpathlist : "+str(nearpathlist))
            meet.append(nearmeet)
            return (meet,kaisatu,nearpathlist)

        #重複数に偏りがあるとき
        for n in range(lineNum):
            from_kaisatu_to_dst = sys.maxsize #改札からdstまでの最短距離保持(改札決定用)
            for i in src[n][1]:
                d, v = solve(route_map, nTown, i, dst)
                if d<from_kaisatu_to_dst:
                    from_kaisatu_to_dst = d
                    kaisatu[n] = i
                    print(str(kaisatu[n])+"からの最短:　"+str(d))
                if n==0 and d<maindis:
                    maindis = d
                    mainvia = v
                    mainline = n
            srcdist[n] = maindis
        nearpathlist.append(getPath(dst,mainvia))
        print("")
        print("改札番号： "+str(kaisatu))
        for n in range(lineNum):
            if n!=mainline:
                m,d = meetDist(route_map, nTown, kaisatu[n], dst, mainvia)
                to_dst = srcdist[n]-d
                if to_dst<neardst:
                    neardst = to_dst
                    nearmeet = m
        for n in range(lineNum):
            if n!=mainline:
                d,v = solve(route_map, nTown, kaisatu[n], nearmeet)
                nearpathlist.append(getPath(nearmeet,v))
        print("nearpathlist : "+str(nearpathlist))
        meet.append(nearmeet)
        return (meet,kaisatu,nearpathlist)

    #路線重複なしの時(バラバラ)
    for n in range(lineNum):
        from_kaisatu_to_dst = sys.maxsize
        for i in src[n][1]:
            d, v = solve(route_map, nTown, i, dst)
            print(str(i)+"からの距離 : "+str(d))
            if d<from_kaisatu_to_dst: #各路線からの改札決定
                from_kaisatu_to_dst = d
                kaisatu[n] = i
                print("min")
            if d<maindis: #最短距離のとき
                other=[] #メインルートの人以外の路線
                maindis = d
                mainvia = v
                mainline = n
        srcdist[n] = maindis
    nearpathlist.append(getPath(dst,mainvia))
    print("")
    print("改札番号： "+str(kaisatu))
    for n in range(lineNum):
        if n!=mainline:
            m,d = meetDist(route_map, nTown, kaisatu[n], dst, mainvia)
            to_dst = srcdist[n]-d
            if to_dst<neardst:
                neardst = to_dst
                nearmeet = m
    for n in range(lineNum):
        if n!=mainline:
            d,v = solve(route_map, nTown, kaisatu[n], nearmeet)
            nearpathlist.append(getPath(nearmeet,v))
    print("nearpathlist : "+str(nearpathlist))
    meet.append(nearmeet)
    return (meet,kaisatu,nearpathlist)



"""
   目的地なしの時
       src: 同じ路線を使用する人数と路線の改札を保持した配列
       num: 待ち合わせ人数
       lineNum: 使用路線数
"""
def noDestination(route_map, nTown, src, lineNum):
    maindis = sys.maxsize #目的地までの最短距離
    kaisatu = [] #各路線の改札保持
    goal = sys.maxsize #集まる所人のノード
    meet = [] #合流式、1地点式の両方の待ち合わせ場所を格納
    joinmeet = [] #合流式の待ち合わせ場所を格納
    onemeet = sys.maxsize #1地点(中間地点より)での待ち合わせ場所
    otherkaisatu = [] #出るべき改札を格納
    other_sumdis = 0 #メインルート以外の人の合流地点までの和(1地点待ち合わせ場所算出に利用)
    sumdis = sys.maxsize
    onepathlist = [] #joinmeetに行くための経路のリスト
    print("目的地なしの始点：　"+str(src))

    #重複時含む
    if src[0][0]!=1: #重複している
        if lineNum==1: #全員が同じ路線の時→改札を返す
            for i in src[0][1]:
                #onemeet.append(i)
                onmeet = i
                kaisatu.append(i)
                onepathlist.append([i])
            meet.append(onemeet)
            return (meet,kaisatu,onepathlist)
        if lineNum==2: #使用路線数が2→人数の多い路線の改札に集合するとき
            if src[0][0]==2 and src[1][0]==2: #4人.2.2
                for i in src[0][1]:
                    for j in src[1][1]:
                        d,v = solve(route_map, nTown, i, j)
                        if d<maindis:
                            maindis = d
                            start = i
                            goal = j
                            print("min")
                            mainvia =v
                path = getPath(goal,mainvia)
                half = 0
                print("2人のpath:　"+str(path))
                for i in range(len(path)-1):
                    if half<maindis/2: #中間地点以下なら
                        half = half + route_map[path[i]][path[i+1]]
                        index = i+1
                print("distance: "+str(maindis)+" half: "+str(half))
                kaisatu.extend([start,goal])
                #もう少しきれいにしたい
                d,v = solve(route_map,nTown,goal,path[index])
                onepathlist.append(getPath(path[index],mainvia))
                onepathlist.append(getPath(path[index],v))
                meet.append(path[index])
                return (meet,kaisatu,onepathlist)

            for i in src[0][1]:
                for j in src[1][1]:
                    d,v = solve(route_map, nTown, i, j)
                    print("改札"+str(i)+"から"+str(j)+"の距離： "+str(d))
                    print("改札"+str(i)+"から"+str(j)+"までの経路:　"+str(getPath(j,v)))
                    if d<maindis: #メインルートなら
                        start = i
                        goal = j
                        maindis = d
                        M = i
                        mainvia = v
                        print("goal="+str(goal))
            onepathlist.append(getPath(goal,mainvia))
            kaisatu.extend([start,goal])
            meet.append(M)
            return (meet,kaisatu,onepathlist)

        #以降使用路線数が2以上の時
        if src[0][0]==src[1][0]==2: #5人.2.2.1
            for n in range(lineNum-1):
                for i in src[n][1]:
                    for j in src[n+1][1]:
                        d,v = solve(route_map, nTown, i, j)
                        if d<maindis:
                            maindis = d
                            other=[] #メインルートの人以外の路線
                            goal = j #メインルートの終点
                            start = i #メインルートの始点(デバック用)
                            print("min")
                            mainvia = v
                            for l in range(lineNum):
                                if l!=n and l!=n+1:
                                    other.append(src[l][1])

        else:
            for n in range(lineNum-1):
                for i in src[0][1]: #最大路線重複数
                    for j in src[n+1][1]:
                        d,v = solve(route_map, nTown, i, j)
                        print("改札"+str(i)+"から"+str(j)+"の距離： "+str(d))
                        print("改札"+str(i)+"から"+str(j)+"までの経路:　"+str(getPath(j,v)))
                        if d<maindis:
                            other=[] #メインルートの人以外の路線
                            goal = j #メインルートの終点
                            start = i #メインルートの始点(デバック用)
                            maindis = d
                            print("min")
                            mainvia = v
                            for l in range(lineNum):
                                if l!=0 and l!=n+1:
                                    other.append(src[l][1])
        onepathlist.append(getPath(goal,mainvia))
        print("目的地なしのother：　"+str(other))
        print("mainstart: "+str(start))
        print("maingoal: "+str(goal))
        #メインルート以外の人が合流する地点を算出
        for n in range(len(other)):
            mindis = sys.maxsize #otherそれぞれのmeetへの最短距離
            for i in other[n]:
                m,d= meetDist(route_map, nTown, i, goal, mainvia)
                if d<mindis:
                    mindis = d
                    M = m
                    kai = i #otherからmeetに行くときの最短の改札
            otherkaisatu.append(kai)
            joinmeet.append(M)
        #合流地点(joinmeet)の内otherの距離の差が小さいほう
        for m in joinmeet:
            for i in otherkaisatu:
                d,v = solve(route_map, nTown, i, m)
                other_sumdis = other_sumdis+d
            if other_sumdis<sumdis:
                onemeet = m
        for i in other:
            d,v = solve(route_map, nTown, i, onemeet)
            onepathlist.append(getPath(onemeet,v))
        kaisatu.extend([start,goal])
        for i in otherkaisatu:
            kaisatu.append(i)
        meet.append(onemeet)
        print("改札番号：　"+str(start)+","+str(goal)+","+str(otherkaisatu))
        return (meet,kaisatu,onepathlist)

    #路線重複がないとき(バラバラ)
    for n in range(lineNum):
        stationdis = sys.maxsize #駅から改札までの最短距離を保持
        print(str(n+1)+"人目の改札：　"+str(src[n][1]))
        for i in src[n][1]:
            if (lineNum-1-n)!=0:
                for m in range((lineNum-1-n)):
                    for j in src[m+n+1][1]:
                        d,v = solve(route_map, nTown, i, j)
                        print("改札"+str(i)+"から"+str(j)+"の距離： "+str(d))
                        print("改札"+str(i)+"から"+str(j)+"までの経路:　"+str(getPath(j,v)))
                        if d<maindis:
                            other=[] #メインルートの人以外の路線
                            goal = j #メインルートの終点
                            start = i #メインルートの始点(デバック用)
                            maindis = d
                            print("min")
                            mainvia = v
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
        d,v = solve(route_map,nTown,goal,path[index])
        onepathlist.append(getPath(path[index],mainvia))
        onepathlist.append(getPath(path[index],v))
        print("distance: "+str(maindis)+" half: "+str(half))
        meet.append(path[index])
        return (meet,kaisatu,onepathlist)

    onepathlist.append(getPath(goal,mainvia))
    for n in range(len(other)):
        mindis = sys.maxsize #otherそれぞれのmeetへの最短距離
        for i in other[n]:
            m,d= meetDist(route_map, nTown, i, goal, mainvia)
            if d<mindis:
                mindis = d
                M = m
                kai = i #otherからmeetに行くときの最短の改札
        otherkaisatu.append(kai)
        joinmeet.append(M)
    #合流地点(joinmeet)の内otherの距離の差が小さいほう
    for m in joinmeet:
        for i in otherkaisatu:
            d,v = solve(route_map, nTown, i, m)
            other_sumdis = other_sumdis+d
        if other_sumdis<sumdis:
            onemeet = m
    for i in other:
        d,v = solve(route_map, nTown, i, onemeet)
        onepathlist.append(getPath(onemeet,v))
    for i in otherkaisatu:
        kaisatu.append(i)
    meet.append(onemeet)
    print("改札番号：　"+str(start)+","+str(goal)+","+str(otherkaisatu))
    return (meet,kaisatu,onepathlist)


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
   改札を決定する
       src: 路線の利用数、路線の改札の配列
       lineNum: 利用路線数
"""
def decideGate(n,src,lineNum):
    usekaisatu = np.array(sys.maxsize*lineNum) #初期化
    from_kaisatu_to_dst = sys.maxsize #各改札までの最短距離保持
    for i in src[n][1]:
        d, v = solve(route_map, nTown, i, dst)
        print(str(i)+"からの距離 : "+str(d))
        if d<from_kaisatu_to_dst: #各路線からの改札決定
            from_kaisatu_to_dst = d
            usekaisatu[n] = i
    return(d,v,usekaisatu)


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
