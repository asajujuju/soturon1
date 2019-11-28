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
    kaisatu = []
    print("num "+str(num))
    print(src)
    if dest: #目的地ありの時
     return Destination(route_map, nTown, src, dst, num)
    else: #目的地なしの時
     return noDestination(route_map, nTown, src, num)

"""
    #各路線と改札のノード番号をつなぐ
    #for i in range(num):
        #if src[i]==0: #西武新宿駅
            #seibu = [12,13]
            #kaisatu.append(seibu)
        #if src[i]==1: #丸の内線　新宿三丁目
            #maru3 = [14,15]
            #kaisatu.append(maru3)
        #if src[i]==2: #都営新宿　新宿三丁目
            #toei3 = [16]
            #kaisatu.append(toei3)
        #if src[i]==3: #副都心線　新宿三丁目
            fuku3 = [17,18,19]
            kaisatu.append(fuku3)
        if src[i]==4: #丸の内線　新宿
            maru = [20,21]
            kaisatu.append(maru)
        if src[i]==5: #大江戸線　新宿西口
            oedonishi = [22,23]
            kaisatu.append(oedonishi)
        if src[i]==6: #JR 新宿
            jr = [24,25,26,27,28,29,30,31,32,33]
            kaisatu.append(jr)
        if src[i]==7: #小田急　新宿
            odakyu = [25,34,35,36]
            kaisatu.append(odakyu)
        if src[i]==8: #京王線　新宿
            keiou = [25,37,38]
            kaisatu.append(keiou)
        if src[i]==9: #大江戸線　新宿
            oedo = [40,41,42]
            kaisatu.append(oedo)
        if src[i]==10: #都営新宿　新宿
            toei = [40,41]
            kaisatu.append(toei)
        if src[i]==11: #京王新線　新宿
            keioushin = [40,41]
            kaisatu.append(keioushin)

    print(kaisatu)
    print(len(kaisatu))
    for i in range(len(kaisatu)):
        print(kaisatu[i])
        for j in range(len(kaisatu[i])):
            print(kaisatu[i][j])


 if dest: #目的地ありの時
  return Destination(route_map, nTown, src, dst, num)
 else: #目的地なしの時
  return noDestination(route_map, nTown, src, num)
 """


"""
   目的地あり
"""
"""
def Destination(route_map, nTown, src, dst, num):
    maindis = sys.maxsize #目的地までの最短距離
    mainvia = [0]*nTown #目的地までの経路情報を保持する
    #メインルートを決定
    for n in range(num):
        d, v = solve(route_map, nTown, src[n], dst)
        print("距離 : "+str(d))
        print(getPath(dst,v))
        if d<maindis:
            other=[] #メインルートの人以外の路線
            maindis = d
            for i in range(len(v)):
                mainvia[i] = v[i]
            for j in range(num):
                if j!=n:
                    other.append(src[j])
    print("目的地あり:　"+str(other))
    meet = [] #待ち合わせの場所のノードを保持
    for i in range(len(other)):
        m = meetDist(route_map, nTown, other[i], dst, mainvia)
        meet.append(m)
    return meet
"""

"""
   目的地あり
"""
def Destination(route_map, nTown, src, dst, num):
    maindis = sys.maxsize #目的地までの最短距離
    mainvia = [0]*nTown #目的地までの経路情報を保持する
    kaisatu = [sys.maxsize]*num #各路線の改札保持
    mainman = sys.maxsize #メインルートの始点の人
    print(src)
    #メインルートを決定
    for n in range(num):
        stationdis = sys.maxsize #駅から改札までの最短距離保持
        for k in range(len(src[n])):
            print("dst: "+str(dst))
            print("src: "+str(src))
            d, v = solve(route_map, nTown, src[n][k], dst)
            print(str(src[n][k])+"からの距離 : "+str(d))
            #print(getPath(dst,v))
            if d<stationdis: #各路線からの改札決定
                stationdis = d
                kaisatu[n] = src[n][k]
                print("min")
            if d<maindis: #最短距離のとき
                other=[] #メインルートの人以外の路線
                maindis = d
                for i in range(len(v)):
                    mainvia[i] = v[i]
                mainman = n
    for j in range(num):
        if j!=mainman:
            other.append(kaisatu[j])
    print("")
    print("改札番号： "+str(kaisatu))
    print("目的地あり:　"+str(other))
    meet = [] #待ち合わせの場所のノードを保持
    for i in range(len(other)):
        m,d = meetDist(route_map, nTown, other[i], dst, mainvia)
        meet.append(m)
    return meet


"""
   目的地なしの時
"""
"""
def noDestination(route_map, nTown, src, num):
    maindis = sys.maxsize #目的地までの最短距離
    mainvia = [0]*nTown #目的地までの経路情報を保持する
    goal = sys.maxsize
    print("目的地noの始点：　"+str(src))
    for i in range(num):
        if (num-1-i)!=0:
            for j in range((num-1-i)):
                d,v = solve(route_map, nTown, src[i], src[j+i+1])
                if d<maindis:
                    other=[] #メインルートの人以外の路線
                    goal = src[j+i+1] #メインルートの終点
                    start = src[i] #メインルートの始点(デバック用)
                    maindis = d
                    for n in range(len(v)):
                        mainvia[n] = v[n]
                    for k in range(num):
                        if k!=(j+i+1) and k!=i:
                            other.append(src[k])
    print("目的地noのother：　"+str(other))
    print("mainstart: "+str(start))
    print("maingoal: "+str(goal))
    meet = []
    if num==2:
        path = getPath(goal,mainvia)
        half = 0
        for i in range(len(path)-1):
            if half<maindis/2: #中間地点以下なら
                half = half + route_map[path[i]][path[i+1]]
                index = i+1
                meet = path[index]
        return meet
    for i in range(len(other)):
        m = meetDist(route_map, nTown, other[i], goal, mainvia)
        meet.append(m)
    return meet
"""

"""
   目的地なしの時
"""
def noDestination(route_map, nTown, src, num):
    maindis = sys.maxsize #目的地までの最短距離
    mainvia = [0]*nTown #目的地までの経路情報を保持する
    goal = sys.maxsize
    print("目的地なしの始点：　"+str(src))
    for n in range(num):
        stationdis = sys.maxsize #駅から改札までの最短距離を保持
        print(str(n+1)+"人目の改札：　"+str(src[n]))
        for m in range(len(src[n])):
            if (num-1-n)!=0:
                for j in range((num-1-n)):
                    for l in range(len(src[j+n+1])):
                        d,v = solve(route_map, nTown, src[n][m], src[j+n+1][l])
                        print("改札"+str(src[n][m])+"から"+str(src[j+n+1][l])+"の距離： "+str(d))
                        print("改札"+str(src[n][m])+"から"+str(src[j+n+1][l])+"までの経路:　"+str(getPath(src[j+n+1][l],v)))
                        if d<maindis:
                            other=[] #メインルートの人以外の路線
                            goal = src[j+n+1][l] #メインルートの終点
                            start = src[n][m] #メインルートの始点(デバック用)
                            maindis = d
                            print("min")
                            for i in range(len(v)):
                                mainvia[i] = v[i]
                            for k in range(num):
                                if k!=(j+n+1) and k!=n:
                                    other.append(src[k])
    print("目的地なしのother：　"+str(other))
    print("mainstart: "+str(start))
    print("maingoal: "+str(goal))
    otherkaisatu = [] #出るべき改札を格納
    meet = [] #最短経路で合流できるノード格納
    if num==2:
        path = getPath(goal,mainvia)
        half = 0
        for i in range(len(path)-1):
            if half<maindis/2: #中間地点以下なら
                half = half + route_map[path[i]][path[i+1]]
                index = i+1
        meet.append(path[index])
        return meet
    for n in range(len(other)):
        mindis = sys.maxsize #otherそれぞれのmeetへの最短距離
        for i in range(len(other[n])):
            m,d = meetDist(route_map, nTown, other[n][i], goal, mainvia)
            if d<mindis:
                mindis = d
                M = m
                kaisatu = other[n][i] #otherからmeetに行くときの最短の改札
        otherkaisatu.append(kaisatu)
        meet.append(M)
    print("改札番号：　"+str(start)+","+str(goal)+","+str(otherkaisatu))
    return meet


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
        #print(marked)
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
