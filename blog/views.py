from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Group, Route, Cafe
from .forms import GroupForm, RouteForm
import numpy
from .RunDijkstra_t import Run

# Create your views here.

"""
8000にアクセスした時
index.htmlを表示する
"""
def index(request):
    return render(request, 'blog/index.html')


"""
index.htmlの待ち合わせボタンを押した時:
   else文を実行してselect.htmlを表示する

select.htmlでSaveボタンを押した時:
   先頭のif文を実行して
      ・select.htmlのフォームに入力された内容を取得、値の正誤チェックを行う
      ・正誤チェックをクリアしたらデータベース(Group)に値を保存する
      ・map.htmlにリダイレクトする
"""
def select(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            return redirect('map', pk=group.pk)
    else:
        form = GroupForm()
    return render(request, 'blog/select.html', {'form': form})



def FileRead(t):
    #ファイルを読み込む
    file_data = open(t, "r")
    firstline = True
    #読み込んだファイルを1行ずつ表示
    exit = []
    for line in file_data:
        data = line.split(' ')#空白文字で区切る
        userval = str(data[0])#データベースに入れる値
        dbval = int(data[1])#ユーザーが見る値
        exit.append([dbval, userval])#出口
    #開いたファイルを閉じる
    file_data.close()
    return(exit)


"""
改札場合わけのためのファイル読み込み
startrout.txtを読み込む
"""
def GateFileRead():
    #ファイルを読み込む
    file_data = open("startroute.txt", "r")
    firstline = True
    #読み込んだファイルを1行ずつ表示
    StationSize = []
    for line in file_data:
        data = line.split(' ')#空白文字で区切る
        station = int(data[0])#駅のノード
        gate = int(data[1])#改札のノード
        dis = int(data[2])#駅から改札までの距離
        StationSize.append([station, gate, dis])#各駅の改札までの距離情報
    #開いたファイルを閉じる
    file_data.close()
    return(StationSize)


"""
最適解を待ち合わせポイントに変換
"""
def point(meet_node):
    #ファイルを読み込む
    file_data = open("point.txt", "r")
    firstline = True
    #読み込んだファイルを1行ずつ表示
    MeetToPoint = []
    for line in file_data:
        data = line.split(' ')#空白文字で区切る
        meet = int(data[0])#駅のノード
        point = int(data[1])#改札のノード
        MeetToPoint.append([meet,point])#各駅の改札までの距離情報
    #開いたファイルを閉じる
    file_data.close()
    #pの初期値
    p = []
    #mの情報をpointに変換
    for case in meet_node:
        for m in case:
            for index, item in enumerate(MeetToPoint):
                if MeetToPoint[index][0] == m:
                    p.append(MeetToPoint[index][1])#待ち合わせ場所
    #pの配列が空の時
    if not p:
        p.append(m)#元の最適解
    #値を返す
    return p


"""
select.htmlやadd.htmlでSaveボタンを押した時のリダイレクト先。
Groupテーブル、Routeテーブルから必要なオブジェクトを取り出し、
そのオブジェクトをmap.htmlに与えて表示させる
"""
def map(request, pk):
    group = get_object_or_404(Group, pk=pk)
    routes = Route.objects.filter(number=pk)
    length = routes.count()
    dest = False #目的地の有無
    mark = 0 #ランドマークor出口のノード番号
    meet = [-100, -100, -100]

    rn = []
    for r in routes:
        rn.append(r.route)

    route = []
    Routemarks = FileRead("route.txt")

    for land in Routemarks:
        for i in rn:
            if i == land[0]:
                route.append(land[1])

    landmark = "なし"
    if group.destination:
        dest = True
        if group.landmark != -1:
            mark = group.landmark
            Landmarks = FileRead("landmark.txt")
            for land in Landmarks:
                if mark == land[0]:
                    landmark = land[1]
        else:
            mark = group.exitmark
            Exitmarks = FileRead("exit.txt")
            for land in Exitmarks:
                if mark == land[0]:
                    landmark = land[1]

    #使用する駅ごとの改札番号を割り出す
    station = GateFileRead()#startroute.txtの中身
    stationNo = [x[0] for x in station]#駅番号
    gateNo = [x[1] for x in station]#改札番号
    p = []#使用する駅
    for r in routes:
        p.append(r.route)
    print(p)
    line = [] #meetに与える路線の引数
    #lineの中身
    for index, item in enumerate(p):
        a = []
        for index2, item2 in enumerate(stationNo):
            if item == item2:
                a.append(gateNo[index2])
        line.append(a)
    #print(line)

    if length == group.people:
        meet, kaisatu = Run(p, mark, dest) #待ち合わせの最適解
        print(meet)
        #meet2 = point(meet)
    return render(request, 'blog/map.html', {'landmark': landmark,'route': route, 'group': group, 'routes': routes, 'meet': meet, 'length': length,})



"""
mapページ内の追加ボタンを押した時
"""
def add_route(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            route = form.save(commit="False")
            route.number = pk
            route.save()
            return redirect('map', pk=route.number)
    else:
        form = RouteForm()
    return render(request, 'blog/add_route.html', {'form': form})
