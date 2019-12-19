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
ファイル読み込み
"""
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
select.htmlやadd.htmlでSaveボタンを押した時のリダイレクト先。
Groupテーブル、Routeテーブルから必要なオブジェクトを取り出し、
そのオブジェクトをmap.htmlに与えて表示させる
"""
def map(request, pk):
    group = get_object_or_404(Group, pk=pk)
    routes = Route.objects.filter(number=pk)
    rn = []
    for r in routes:
        rn.append(r.route)
    
    route = []
    Routemarks = FileRead("route.txt")
   
    for land in Routemarks:
        for i in rn:
            if i == land[0]:
                route.append(land[1])
            
    #cafes = Cafe.objects.all()
    len = routes.count()
    dest = False #目的地の有無
    mark = 0 #ランドマークor出口のノード番号
    meet = [-100, -100, -100]

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
    if len == group.people:
        meet = Run([220, 217], mark, dest) #待ち合わせの最適解           
                        
    return render(request, 'blog/map.html', {'landmark': landmark,'route': route, 'group': group, 'routes': routes, 'meet': meet, 'len': len})


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



"""
mapページの路線変更ボタンを押した時
"""
def change_route(request, group_num, pk):
    Route.objects.filter(pk = pk).delete()
    return redirect('add_route', pk=group_num)
