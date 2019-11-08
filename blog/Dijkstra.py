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
    dis = np.zeros(num)
    via = []
    #待ち合わせの人数分の目的地への最短経路を保持
    for n in range(num):
        d, v = solve(route_map, nTown, src[n], dst)
        dis[n] = d
        via.append(v)
    if len(dis)==2:
        return two(route_map, nTown, src, dst, dest, dis, via)
    if len(dis)==3:
        return three(route_map, nTown, src, dst, dest, dis, via)

"""
   待ち合わせ人数が3人の時
"""
def three(route_map, nTown, src, dst, dest, dis, via):
    meet = []
    if dest==True: #目的地があるとき
        print(dis[0])
        print(getPath(dst,via[0]))
        print(dis[1])
        print(getPath(dst,via[1]))
        print(dis[2])
        print(getPath(dst,via[2]))
        if dis[0]<dis[1]:
            if dis[0]<dis[2]:
                m = meetDist(route_map, nTown, src[2], dst, via[0])
                meet.append(m)
                m = meetDist(route_map, nTown, src[1], dst, via[0])
                meet.append(m)
                return meet
            else:
                m = meetDist(route_map, nTown, src[0], dst, via[2])
                meet.append(m)
                m = meetDist(route_map, nTown, src[1], dst, via[2])
                meet.append(m)
                return meet
        else:
            if dis[1]<dis[2]:
                m = meetDist(route_map, nTown, src[0], dst, via[1])
                meet.append(m)
                m = meetDist(route_map, nTown, src[2], dst, via[1])
                meet.append(m)
                return meet
            else:
                m = meetDist(route_map, nTown, src[0], dst, via[2])
                meet.append(m)
                m = meetDist(route_map, nTown, src[1], dst, via[2])
                meet.append(m)
                return meet
    else: #目的地なし
        d0, v0 = solve(route_map, nTown, src[0], src[1])
        d1, v1 = solve(route_map, nTown, src[0], src[2])
        d2, v2 = solve(route_map, nTown, src[1], src[2])
        print(getPath(src[1],v0))
        print(getPath(src[2],v1))
        print(getPath(src[2],v2))
        if d0<d1:
            if d0<d2:
                meet = meetDist(route_map, nTown, src[2], src[1], v0)
                return meet
            else:
                meet = meetDist(route_map, nTown, src[0], src[2], v2)
                return meet
        else:
            if d1<d2:
                meet = meetDist(route_map, nTown, src[1], src[2], v1)
                return meet
            else:
                meet = meetDist(route_map, nTown, src[0], src[2], v2)
                return meet


"""
   待ち合わせ人数が2人の時
"""
def two(route_map, nTown, src, dst, dest, dis, via):
    if dest==True: #目的地があるとき
        print(dis[0])
        print(getPath(dst,via[0]))
        print(dis[1])
        print(getPath(dst,via[1]))
        if dis[0]<dis[1]:
            return meetDist(route_map, nTown, src[1], dst, via[0])
        else:
            return meetDist(route_map, nTown, src[0], dst, via[1])
    else: #目的地なし
        return meet(route_map, nTown, src)

"""
   目的地ありの時
   最短距離で出会うノードを探索するメソッド
"""
def meetDist(route_map, nTown, src, dst, via):
    via_kari = getPath(dst,via)
    dist = sys.maxsize
    for i in range(len(via_kari)):
        d, v = solve(route_map, nTown, src, via_kari[i])
        if d<dist:
            dist = d
            meet = via_kari[i]
    return meet

"""
   目的地なしの時
   最短距離で出会うノードを探索するメソッド
"""
def meet(route_map, nTown, src):
    dis, via = solve(route_map, nTown, src[0], src[1])
    path = getPath(src[1],via)
    print(path)
    half = 0
    node = path[0]
    for i in range(len(path)-1):
        if half<dis/2:
            half = half + route_map[path[i]][path[i+1]]
            node = i+1
    meet = path[node]
    return meet

"""
   最短経路探索を行うメソッド
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
            return
        if distance[marked]==sys.maxsize: #非連結グラフ→つながっていないと無限大のまま
            return
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
