import sys
import numpy as np

"""
   目的地がありの時の最短経路検索
       num: 待ち合わせする人の数
       member: 待ち合わせする人のノード番号を保持した配列
       goal: 目的地のノード番号
"""

"""
   待ち合わせ場所の解を返すメソッド
"""
def answer(route_map, nTown, src, dst, dest):
    if dest==True: #目的地があるとき
        dis1, via1 = solve(route_map, nTown, src[0], dst)
        dis2, via2 = solve(route_map, nTown, src[1], dst)
        print(dis1)
        print(getPath(dst,via1))
        print(dis2)
        print(getPath(dst,via2))
        if dis1<dis2:
            via_kari = getPath(dst, via1)
            dist = sys.maxsize
            for i in range(len(via_kari)):
                d, v = solve(route_map, nTown, src[1], via_kari[i])
                if d<dist:
                    dist = d
                    meet = via_kari[i]
            return meet
        else:
            via = getPath(dst, via1)
            dist = sys.maxsize
            for i in range(len(via)):
                d, v = solve(route_map, nTown, src[0], via[i])
                if d<dist:
                    final_d = d
                    meet = v[i]
            return meet
    else: #目的地なし
        dis1, via1 = solve(route_map, nTown, src[0], src[1])
        path = getPath(src[1],via1)
        print(path)
        half = int(len(path)/2)
        meet = path[half]
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
