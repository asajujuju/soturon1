
# -*- coding: utf-8 -*-
import numpy as np
from .Dijkstra_mokuteki2 import answer

"""
   地図ファイルを読み込むメソッド
"""
def FileRead():
    #ファイルを読み込む
    #file_data = open("nanana3.pythonanywhere.com/shinjukuroute.txt", "r")
    file_data = open("shinjukuroute.txt", "r")
    firstline = True
    #読み込んだファイルを1行ずつ表示
    for line in file_data:
        if firstline:#firstlineがtureの時=1行目の時
            data = line.split(' ')#空白文字で区切る
            nTown = int(data[0])#ノード数
            nRoute = int(data[1])#エッジの数
            route_map=np.zeros((nTown, nTown))#都市の接続関係マップ
            for i in range(nTown):#接続のマップを初期化する
                for j in range(nTown):
                    """
                       ↓三項演算子
                        (条件がtrueの時の値) if (条件) else (条件がfalseの時の値)
                    """
                    route_map[i][j] = 0 if i==j else -1
                    firstline = False#最初の行が終了
        else:#2行目以降
            data = line.split(" ",3)
            from_r = int(data[0])
            to_r = int(data[1])
            len_r = int(data[2])
            route_map[from_r][to_r] = len_r
            route_map[to_r][from_r] = len_r
            #開いたファイルを閉じる
    file_data.close()
    return(route_map, nTown)


"""
   最短距離を受け取るメソッド
"""
def Run(src, dst, dest):
    route_map, nTown = FileRead()
    meet = answer(route_map, nTown, src, dst, dest)
    print(meet)
    list = src
    list.insert(0,meet)
    print(list)
    return list

#Run([220, 217], 32, False)
