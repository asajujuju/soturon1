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
select.htmlやadd.htmlでSaveボタンを押した時のリダイレクト先。
Groupテーブル、Routeテーブルから必要なオブジェクトを取り出し、
そのオブジェクトをmap.htmlに与えて表示させる
"""
def map(request, pk):
    group = get_object_or_404(Group, pk=pk)
    routes = Route.objects.filter(number=pk)
    #cafes = Cafe.objects.all()
    len = routes.count()
    dest = False #目的地の有無
    mark = 0 #ランドマークor出口のノード番号
    meet = [-100, -100, -100]
    if group.destination:
        dest = True
        if group.landmark != -1:
            mark = group.landmark
        else:
            mark = group.exitmark

    #使用する駅ごとの改札番号を割り出す
    station = GateFileRead()#startroute.txtの中身
    stationNo = [x[0] for x in station]#駅番号
    gateNo = [x[1] for x in station]#改札番号
    p = [0,2]#使用する駅
    line = []#meetに与える路線の引数
    #lineの中身
    for index, item in enumerate(p):
        a = []
        for index2, item2 in enumerate(stationNo):
            if item == item2:
                a.append(gateNo[index2])
        line.append(a)
    print(line)

    if len == group.people:
        meet = Run([220, 217], mark, dest) #待ち合わせの最適解
    return render(request, 'blog/map.html', {'group': group, 'routes': routes, 'meet': meet, 'len': len})



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
