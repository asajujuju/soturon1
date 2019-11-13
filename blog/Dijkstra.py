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
    dis = np.zeros(num) #目的地までの距離を保持する
    via = [] #目的地までの経路情報を保持する

    #待ち合わせの人数分の目的地への最短経路を保持
    for n in range(num):
        d, v = solve(route_map, nTown, src[n], dst)
        dis[n] = d
        via.append(v)
    if num==2:
        return two(route_map, nTown, src, dst, dest, dis, via)
    if num==3:
        return three(route_map, nTown, src, dst, dest, dis, via)
    if num==4:
        return four(route_map, nTown, src, dst, dest, dis, via)
    if num==5:
        return five(route_map, nTown, src, dst, dest, dis, via)

"""
   待ち合わせ人数が五人の時
      src: それぞれの路線のノード番号を保持した配列
      dst: 目的地のノード番号
      dest: 目的地の有無
      dis: 目的地までの各路線からの距離を保持した配列
      via: 目的地までの経路情報を保持した配列
"""
def five(route_map, nTown, src, dst, dest, dis, via):
    meet = [] #待ち合わせの場所のノードを保持
    if dest==True: #目的地があるとき
        if dis[0]<dis[1]:
            if dis[0]<dis[2]:
                if dis[0]<dis[3]:
                    if dis[0]<dis[4]:
                        m = meetDist(route_map, nTown, src[1], dst, via[0])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[2], dst, via[0])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[3], dst, via[0])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[4], dst, via[0])
                        meet.append(m)
                        return meet
                    else:
                        m = meetDist(route_map, nTown, src[0], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[1], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[2], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[3], dst, via[4])
                        meet.append(m)
                        return meet
                else: #dis[3]<dis[0]<dis[2]
                    if dis[3]<dis[4]:
                        m = meetDist(route_map, nTown, src[0], dst, via[3])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[1], dst, via[3])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[2], dst, via[3])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[4], dst, via[3])
                        meet.append(m)
                        return meet
                    else:
                        m = meetDist(route_map, nTown, src[0], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[1], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[2], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[3], dst, via[4])
                        meet.append(m)
                        return meet
            else: #dis[2]<dis[0]
                if dis[2]<dis[3]:
                    if dis[2]<dis[4]:
                        m = meetDist(route_map, nTown, src[0], dst, via[2])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[1], dst, via[2])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[3], dst, via[2])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[4], dst, via[2])
                        meet.append(m)
                        return meet
                    else:
                        m = meetDist(route_map, nTown, src[0], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[1], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[2], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[3], dst, via[4])
                        meet.append(m)
                        return meet
                else: #dis[3]<dis[2]<dis[0]
                    if dis[3]<dis[4]:
                        m = meetDist(route_map, nTown, src[0], dst, via[3])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[1], dst, via[3])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[2], dst, via[3])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[4], dst, via[3])
                        meet.append(m)
                        return meet
                    else:
                        m = meetDist(route_map, nTown, src[0], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[1], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[2], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[3], dst, via[4])
                        meet.append(m)
                        return meet
        else: #dis[1]<dis[0]
            if dis[1]<dis[2]:
                if dis[1]<dis[3]:
                    if dis[1]<dis[4]:
                        m = meetDist(route_map, nTown, src[0], dst, via[1])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[2], dst, via[1])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[3], dst, via[1])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[4], dst, via[1])
                        meet.append(m)
                        return meet
                    else:
                        m = meetDist(route_map, nTown, src[0], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[1], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[2], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[3], dst, via[4])
                        meet.append(m)
                        return meet
                else: #dis[3]<dis[1]<dis[2]
                    if dis[3]<dis[4]:
                        m = meetDist(route_map, nTown, src[0], dst, via[3])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[1], dst, via[3])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[2], dst, via[3])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[4], dst, via[3])
                        meet.append(m)
                        return meet
                    else:
                        m = meetDist(route_map, nTown, src[0], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[1], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[2], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[3], dst, via[4])
                        meet.append(m)
                        return meet
            else: #dis[2]<dis[1]
                if dis[2]<dis[3]:
                    if dis[2]<dis[4]:
                        m = meetDist(route_map, nTown, src[0], dst, via[2])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[1], dst, via[2])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[3], dst, via[2])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[4], dst, via[2])
                        meet.append(m)
                        return meet
                    else:
                        m = meetDist(route_map, nTown, src[0], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[1], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[2], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[3], dst, via[4])
                        meet.append(m)
                        return meet
                else: #dis[3]<dis[2]<dis[1]
                    if dis[3]<dis[4]:
                        m = meetDist(route_map, nTown, src[0], dst, via[3])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[1], dst, via[3])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[2], dst, via[3])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[4], dst, via[3])
                        meet.append(m)
                        return meet
                    else:
                        m = meetDist(route_map, nTown, src[0], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[1], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[2], dst, via[4])
                        meet.append(m)
                        m = meetDist(route_map, nTown, src[3], dst, via[4])
                        meet.append(m)
                        return meet
    else: #目的地なし
        d0, v0 = solve(route_map, nTown, src[0], src[1])
        d1, v1 = solve(route_map, nTown, src[0], src[2])
        d2, v2 = solve(route_map, nTown, src[0], src[3])
        d3, v3 = solve(route_map, nTown, src[0], src[4])
        print(str(d0)+" "+str(d1)+" "+str(d2)+" "+str(d3))
        print(getPath(src[1],v0))
        print(getPath(src[2],v1))
        print(getPath(src[3],v2))
        print(getPath(src[4],v3))
        if d0<d1:
            if d0<d2:
                if d0<d3:
                    d4, v4 = solve(route_map, nTown, src[2], src[3])
                    d5, v5 = solve(route_map, nTown, src[4], src[3])
                    if d0<d4:
                        if d0<d5:
                            d6, v6 = solve(route_map, nTown, src[2], src[1])
                            d7, v7 = solve(route_map, nTown, src[3], src[1])
                            d8, v8 = solve(route_map, nTown, src[4], src[1])
                            distance = [d0,d6,d7,d8]
                            keiro = [v0,v6,v7,v8]
                            start = [src[0],src[2],src[3],src[4]]
                            goal = src[1]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                        else: #d5<d0
                            d6, v6 = solve(route_map, nTown, src[1], src[3])
                            distance = [d2,d4,d5,d6]
                            keiro = [v2,v4,v5,v6]
                            start = [src[0],src[2],src[4],src[1]]
                            goal = src[3]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                    else: #d4<d0
                        d6, v6 = solve(route_map, nTown, src[1], src[3])
                        distance = [d2,d4,d5,d6]
                        keiro = [v2,v4,v5,v6]
                        start = [src[0],src[2],src[4],src[1]]
                        goal = src[3]
                        return four(route_map, nTown, start, goal, True, distance, keiro)
                else: #d3<d0
                    d4, v4 = solve(route_map, nTown, src[3], src[2])
                    d5, v5 = solve(route_map, nTown, src[1], src[2])
                    if d3<d4:
                        if d3<d5:
                            d6, v6 = solve(route_map, nTown, src[1], src[4])
                            d7, v7 = solve(route_map, nTown, src[2], src[4])
                            d8, v8 = solve(route_map, nTown, src[3], src[4])
                            distance = [d3,d6,d7,d8]
                            keiro = [v3,v6,v7,v8]
                            start = [src[0],src[1],src[2],src[3]]
                            goal = src[4]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                        else: #d5<d3
                            d6, v6 = solve(route_map, nTown, src[4], src[2])
                            distance = [d1,d4,d5,d6]
                            keiro = [v1,v4,v5,v6]
                            start = [src[0],src[3],src[1],src[4]]
                            goal = src[2]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                    else: #d4<d3
                        d6, v6 = solve(route_map, nTown, src[4], src[2])
                        distance = [d1,d4,d5,d6]
                        keiro = [v1,v4,v5,v6]
                        start = [src[0],src[3],src[1],src[4]]
                        goal = src[2]
                        return four(route_map, nTown, start, goal, True, distance, keiro)
            else: #d2<d0
                if d2<d3:
                    d4, v4 = solve(route_map, nTown, src[2], src[1])
                    d5, v5 = solve(route_map, nTown, src[4], src[1])
                    if d2<d4:
                        if d2<d5:
                            d6, v6 = solve(route_map, nTown, src[1], src[3])
                            d7, v7 = solve(route_map, nTown, src[2], src[3])
                            d8, v8 = solve(route_map, nTown, src[4], src[3])
                            distance = [d2,d6,d7,d8]
                            keiro = [v2,v6,v7,v8]
                            start = [src[0],src[1],src[2],src[4]]
                            goal = src[3]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                        else: #d5<d2
                            d6, v6 = solve(route_map, nTown, src[3], src[1])
                            distance = [d0,d4,d5,d6]
                            keiro = [v0,v4,v5,v6]
                            start = [src[0],src[2],src[4],src[3]]
                            goal = src[1]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                    else: #d4<d2
                        d6, v6 = solve(route_map, nTown, src[3], src[1])
                        distance = [d0,d4,d5,d6]
                        keiro = [v0,v4,v5,v6]
                        start = [src[0],src[2],src[4],src[3]]
                        goal = src[1]
                        return four(route_map, nTown, start, goal, True, distance, keiro)
                else: #d3<d2
                    d4, v4 = solve(route_map, nTown, src[3], src[2])
                    d5, v5 = solve(route_map, nTown, src[1], src[2])
                    if d3<d4:
                        if d3<d5:
                            d6, v6 = solve(route_map, nTown, src[1], src[4])
                            d7, v7 = solve(route_map, nTown, src[2], src[4])
                            d8, v8 = solve(route_map, nTown, src[3], src[4])
                            distance = [d3,d6,d7,d8]
                            keiro = [v3,v6,v7,v8]
                            start = [src[0],src[1],src[2],src[3]]
                            goal = src[4]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                        else: #d5<d3
                            d6, v6 = solve(route_map, nTown, src[4], src[2])
                            distance = [d1,d4,d5,d6]
                            keiro = [v1,v4,v5,v6]
                            start = [src[0],src[3],src[1],src[4]]
                            goal = src[2]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                    else: #d4<d3
                        d6, v6 = solve(route_map, nTown, src[4], src[2])
                        distance = [d1,d4,d5,d6]
                        keiro = [v1,v4,v5,v6]
                        start = [src[0],src[3],src[1],src[4]]
                        goal = src[2]
                        return four(route_map, nTown, start, goal, True, distance, keiro)
        else: #d1<d0
            if d1<d2:
                if d1<d3:
                    d4, v4 = solve(route_map, nTown, src[1], src[4])
                    d5, v5 = solve(route_map, nTown, src[3], src[4])
                    if d1<d4:
                        if d1<d5:
                            d6, v6 = solve(route_map, nTown, src[1], src[2])
                            d7, v7 = solve(route_map, nTown, src[3], src[2])
                            d8, v8 = solve(route_map, nTown, src[4], src[2])
                            distance = [d1,d6,d7,d8]
                            keiro = [v1,v6,v7,v8]
                            start = [src[0],src[1],src[3],src[4]]
                            goal = src[2]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                        else: #d5<d1
                            d6, v6 = solve(route_map, nTown, src[2], src[4])
                            distance = [d3,d4,d5,d6]
                            keiro = [v3,v4,v5,v6]
                            start = [src[0],src[1],src[3],src[2]]
                            goal = src[4]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                    else: #d4<d1
                        d6, v6 = solve(route_map, nTown, src[2], src[4])
                        distance = [d3,d4,d5,d6]
                        keiro = [v3,v4,v5,v6]
                        start = [src[0],src[1],src[3],src[2]]
                        goal = src[4]
                        return four(route_map, nTown, start, goal, True, distance, keiro)
                else: #d3<d1
                    d4, v4 = solve(route_map, nTown, src[3], src[2])
                    d5, v5 = solve(route_map, nTown, src[1], src[2])
                    if d3<d4:
                        if d3<d5:
                            d6, v6 = solve(route_map, nTown, src[1], src[4])
                            d7, v7 = solve(route_map, nTown, src[2], src[4])
                            d8, v8 = solve(route_map, nTown, src[3], src[4])
                            distance = [d3,d6,d7,d8]
                            keiro = [v3,v6,v7,v8]
                            start = [src[0],src[1],src[2],src[3]]
                            goal = src[4]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                        else: #d5<d3
                            d6, v6 = solve(route_map, nTown, src[4], src[2])
                            distance = [d1,d4,d5,d6]
                            keiro = [v1,v4,v5,v6]
                            start = [src[0],src[3],src[1],src[4]]
                            goal = src[2]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                    else: #d4<d3
                        d6, v6 = solve(route_map, nTown, src[4], src[2])
                        distance = [d1,d4,d5,d6]
                        keiro = [v1,v4,v5,v6]
                        start = [src[0],src[3],src[1],src[4]]
                        goal = src[2]
                        return four(route_map, nTown, start, goal, True, distance, keiro)
            else: #d2<d1
                if d2<d3:
                    d4, v4 = solve(route_map, nTown, src[2], src[1])
                    d5, v5 = solve(route_map, nTown, src[4], src[1])
                    if d2<d4:
                        if d2<d5:
                            d6, v6 = solve(route_map, nTown, src[1], src[3])
                            d7, v7 = solve(route_map, nTown, src[2], src[3])
                            d8, v8 = solve(route_map, nTown, src[4], src[3])
                            distance = [d2,d6,d7,d8]
                            keiro = [v2,v6,v7,v8]
                            start = [src[0],src[1],src[2],src[4]]
                            goal = src[3]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                        else: #d5<d2
                            d6, v6 = solve(route_map, nTown, src[3], src[1])
                            distance = [d0,d4,d5,d6]
                            keiro = [v0,v4,v5,v6]
                            start = [src[0],src[2],src[4],src[3]]
                            goal = src[1]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                    else: #d4<d2
                        d6, v6 = solve(route_map, nTown, src[3], src[1])
                        distance = [d0,d4,d5,d6]
                        keiro = [v0,v4,v5,v6]
                        start = [src[0],src[2],src[4],src[3]]
                        goal = src[1]
                        return four(route_map, nTown, start, goal, True, distance, keiro)
                else: #d3<d2
                    d4, v4 = solve(route_map, nTown, src[3], src[2])
                    d5, v5 = solve(route_map, nTown, src[1], src[2])
                    print(str(d4)+" "+str(d5))
                    if d3<d4:
                        if d3<d5:
                            d6, v6 = solve(route_map, nTown, src[1], src[4])
                            d7, v7 = solve(route_map, nTown, src[2], src[4])
                            d8, v8 = solve(route_map, nTown, src[3], src[4])
                            print(str(d6)+" "+str(d7)+" "+str(d8))
                            distance = [d3,d6,d7,d8]
                            keiro = [v3,v6,v7,v8]
                            start = [src[0],src[1],src[2],src[3]]
                            goal = src[4]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                        else: #d5<d3
                            d6, v6 = solve(route_map, nTown, src[4], src[2])
                            distance = [d1,d4,d5,d6]
                            keiro = [v1,v4,v5,v6]
                            start = [src[0],src[3],src[1],src[4]]
                            goal = src[2]
                            return four(route_map, nTown, start, goal, True, distance, keiro)
                    else: #d4<d3
                        d6, v6 = solve(route_map, nTown, src[4], src[2])
                        distance = [d1,d4,d5,d6]
                        keiro = [v1,v4,v5,v6]
                        start = [src[0],src[3],src[1],src[4]]
                        goal = src[2]
                        return four(route_map, nTown, start, goal, True, distance, keiro)



"""
   待ち合わせ人数が四人の時
      src: それぞれの路線のノード番号を保持した配列
      dst: 目的地のノード番号
      dest: 目的地の有無
      dis: 目的地までの各路線からの距離を保持した配列
      via: 目的地までの経路情報を保持した配列
"""
def four(route_map, nTown, src, dst, dest, dis, via):
    meet = [] #待ち合わせ場所のノードを保持
    if dest==True: #目的地があるとき
        if dis[0]<dis[1]:
            if dis[0]<dis[2]:
                if dis[0]<dis[3]:
                    m = meetDist(route_map, nTown, src[3], dst, via[0])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[2], dst, via[0])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[1], dst, via[0])
                    meet.append(m)
                    return meet
                else:
                    m = meetDist(route_map, nTown, src[2], dst, via[3])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[1], dst, via[3])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[0], dst, via[3])
                    meet.append(m)
                    return meet
            else: #dis[2]<dis[0]
                if dis[2]<dis[3]:
                    m = meetDist(route_map, nTown, src[3], dst, via[2])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[1], dst, via[2])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[0], dst, via[2])
                    meet.append(m)
                    return meet
                else:
                    m = meetDist(route_map, nTown, src[2], dst, via[3])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[1], dst, via[3])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[0], dst, via[3])
                    meet.append(m)
                    return meet
        else: #dis[1]<dis[0]
            if dis[1]<dis[2]:
                if dis[1]<dis[3]:
                    m = meetDist(route_map, nTown, src[3], dst, via[1])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[2], dst, via[1])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[0], dst, via[1])
                    meet.append(m)
                    return meet
                else:
                    m = meetDist(route_map, nTown, src[2], dst, via[3])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[1], dst, via[3])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[0], dst, via[3])
                    meet.append(m)
                    return meet
            else: #dis[2]<dis[1]<dis[0]
                if dis[2]<dis[3]:
                    m = meetDist(route_map, nTown, src[3], dst, via[2])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[1], dst, via[2])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[0], dst, via[2])
                    meet.append(m)
                    return meet
                else:
                    m = meetDist(route_map, nTown, src[3], dst, via[1])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[2], dst, via[1])
                    meet.append(m)
                    m = meetDist(route_map, nTown, src[0], dst, via[1])
                    meet.append(m)
                    return meet
    else: #目的地なしの時
        d0, v0 = solve(route_map, nTown, src[0], src[1])
        d1, v1 = solve(route_map, nTown, src[0], src[2])
        d2, v2 = solve(route_map, nTown, src[0], src[3])
        print(getPath(src[1],v0))
        print(getPath(src[2],v1))
        print(getPath(src[2],v2))
        if d0<d1:
            if d0<d2:
                d3, v3 = solve(route_map, nTown, src[2], src[3])
                if d0<d3:
                    d4, v4 = solve(route_map, nTown, src[2], src[1])
                    d5, v5 = solve(route_map, nTown, src[3], src[1])
                    distance = [d0,d4,d5]
                    keiro = [v0,v4,v5]
                    start = [src[0],src[2],src[3]]
                    goal = src[1]
                    return three(route_map, nTown, start, goal, True, distance, keiro)
                else:
                    d4, v4 = solve(route_map, nTown, src[0], src[3])
                    d5, v5 = solve(route_map, nTown, src[1], src[3])
                    distance = [d3,d4,d5]
                    keiro = [v3,v4,v5]
                    start = [src[2],src[0],src[1]]
                    goal = src[3]
                    return three(route_map, nTown, start, goal, True, distance, keiro)
            else: #d2<d0
                d3, v3 = solve(route_map, nTown, src[2], src[1])
                if d2<d3:
                    d4, v4 = solve(route_map, nTown, src[1], src[3])
                    d5, v5 = solve(route_map, nTown, src[2], src[3])
                    distance = [d2,d4,d5]
                    keiro = [v2,v4,v5]
                    start = [src[0],src[1],src[2]]
                    goal = src[3]
                    return three(route_map, nTown, start, goal, True, distance, keiro)
                else:
                    d4, v4 = solve(route_map, nTown, src[3], src[1])
                    distance = [d0,d3,d4]
                    keiro = [v0,v3,v4]
                    start = [src[0],src[2],src[3]]
                    goal = src[1]
                    return three(route_map, nTown, start, goal, True, distance, keiro)
        else: #d1<d0
            if d1<d2:
                d3, v3 = solve(route_map, nTown, src[1], src[3])
                if d1<d3:
                    d4, v4 = solve(route_map, nTown, src[1], src[2])
                    d5, v5 = solve(route_map, nTown, src[3], src[2])
                    distance = [d1,d4,d5]
                    keiro = [v1,v4,v5]
                    start = [src[0],src[1],src[3]]
                    goal = src[2]
                    return three(route_map, nTown, start, goal, True, distance, keiro)
                else:
                    d4, v4 = solve(route_map, nTown, src[2], src[3])
                    distance = [d2,d3,d4]
                    keiro = [v2,v3,v4]
                    start = [src[0],src[1],src[2]]
                    goal = src[3]
                    return three(route_map, nTown, start, goal, True, distance, keiro)
            else: #d2<d1<d0
                d3, v3 = solve(route_map, nTown, src[2], src[1])
                if d2<d3:
                    d4, v4 = solve(route_map, nTown, src[1], src[3])
                    d5, v5 = solve(route_map, nTown, src[2], src[3])
                    distance = [d2,d4,d5]
                    keiro = [v2,v4,v5]
                    start = [src[0],src[1],src[2]]
                    goal = src[3]
                    return three(route_map, nTown, start, goal, True, distance, keiro)
                else:
                    d4, v4 = solve(route_map, nTown, src[3], src[1])
                    distance = [d0,d3,d4]
                    keiro = [v0,v3,v4]
                    start = [src[0],src[2],src[3]]
                    goal = src[1]
                    return three(route_map, nTown, start, goal, True, distance, keiro)



"""
   待ち合わせ人数が3人の時
      src: それぞれの路線のノード番号を保持した配列
      dst: 目的地のノード番号
      dest: 目的地の有無
      dis: 目的地までの各路線からの距離を保持した配列
      via: 目的地までの経路情報を保持した配列
"""
def three(route_map, nTown, src, dst, dest, dis, via):
    meet = [] #待ち合わせ場所のノードを保持
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
        print(src[1])
        d0, v0 = solve(route_map, nTown, src[0], src[1])
        d1, v1 = solve(route_map, nTown, src[0], src[2])
        if d0<d1:
            d2, v2 = solve(route_map, nTown, src[2], src[1])
            print("nondest" + str(getPath(src[1],v0)))
            print(getPath(src[2],v1))
            print(getPath(src[1],v2))
            distance = [d0,d2]
            keiro = [v0,v2]
            start = [src[0],src[2]]
            goal = src[1]
            return two(route_map, nTown, start, goal, True, distance, keiro)
        else:
            d2, v2 = solve(route_map, nTown, src[1], src[2])
            print("nondest" + str(getPath(src[1],v0)))
            print(getPath(src[2],v1))
            print(getPath(src[2],v2))
            distance = [d1,d2]
            keiro = [v1,v2]
            start = [src[0], src[1]]
            goal = src[2]
            return two(route_map, nTown, start, goal, True, distance, keiro)

"""
   待ち合わせ人数が2人の時
      src: それぞれの路線のノード番号を保持した配列
      dst: 目的地のノード番号
      dest: 目的地の有無
      dis: 目的地までの各路線からの距離を保持した配列
      via: 目的地までの経路情報を保持した配列
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
      src: スタート地点
      dst: 目的地
      via: メインルートの経路
"""
def meetDist(route_map, nTown, src, dst, via):
    mainroute = getPath(dst,via) #メインルート
    dist = sys.maxsize #メインルートへの最短距離
    for i in range(len(mainroute)):
        d, v = solve(route_map, nTown, src, mainroute[i])
        if d<dist:
            dist = d
            meet = mainroute[i]
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
    for i in range(len(path)-1):
        if half<dis/2: #中間地点以下なら
            half = half + route_map[path[i]][path[i+1]]
            index = i+1
    meet = path[index]
    return meet

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
