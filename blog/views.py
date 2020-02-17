from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Group, Route, Cafe
from .forms import GroupForm, RouteForm
import numpy as np
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
    errorM = ""
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            if group.destination and group.landmark==-1 and group.exitmark==-1:
                 form = GroupForm()
                 errorM = "入力が正しくありません"
                 return render(request, 'blog/select.html', {'form': form, 'errorM': errorM})
            group.save()
            return redirect('map', pk=group.pk)
        else:
            form = GroupForm()
            return render(request, 'blog/select.html', {'form': form, 'errorM': errorM})

    else:
        form = GroupForm()
        return render(request, 'blog/select.html', {'form': form, 'errorM': errorM})



def read_file(file_name):
    #ファイルを読み込む
    #file_data = open("/home/nanako/nanako.pythonanywhere.com/" + file_name, "r")
    file_data = open(file_name, "r")
    firstline = True
    data = []
    for line in file_data:
        line_each = line.split(' ')
        data.append(line_each)
    file_data.close()
    return(data)


"""
最適解を待ち合わせポイントに変換
"""
def point(meet_node):
    #ファイルを読み込む
    MeetToPoint = read_file("point.txt")
    #pの初期値
    p = []
    #meetの情報をpointに変換
    c = []
    for m in meet_node:
        pp = -1
        for item in MeetToPoint:
            if int(item[0]) == m: #待ち合わせポイントがある時
                pp = int(item[1])#待ち合わせ場所
        if pp == -1: #待ち合わせポイントがない時
            c.append(m)
        else:
            c.append(pp)
    p.append(c) #ケース別で格納
    #値を返す
    return p


"""
 改札番号を改札名に変更
"""
def name(kaisatu):
    #改札一覧のファイルを配列に変換する
    KaisatuName = read_file("kaisatu.txt")

    #kaisatuを名前に変換
    Kname = []
    for node in kaisatu:
        for item in KaisatuName:
            if int(item[0]) == node:
                k = item[1]
                Kname.append([k])
    print(Kname)
    return(Kname)


"""
 重複しているものを消去する
"""
def checker(meet):
    a = []
    for i in meet:
        b = list(set(i))
        a.append(b)
    return a


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
    join = []
    one = []
    kaisatuname = []
    routebox = []
    sort_routbox = []
    params = {}

    #路線が同じ人数を計算
    rn = np.zeros(12)
    for r in routes:
        rn[r.route] = rn[r.route] +1

    print("rn: "+str(rn))
    for index in range(len(rn)):
        if rn[index]!=0:
            routebox.extend([[int(rn[index]),index]])
    print("routebox: "+str(routebox))
    sort_routebox=sorted(routebox, key=lambda x:x[0], reverse=True)
    print("sort_routebox2: "+str(sort_routebox))

    route = []
    all_routes = read_file("route.txt")
    for r in all_routes:
        for n in range(len(sort_routebox)):
            if sort_routebox[n][1] == int(r[1]):
                print("ok!")
                route.extend([[r[0],sort_routebox[n][0]]])

    landmark = "なし"
    if group.destination:
        dest = True
        if group.landmark != -1:
            mark = group.landmark
            Landmarks = read_file("landmark.txt")
            for land in Landmarks:
                if mark == int(land[1]):
                    landmark = land[0]
        else:
            mark = group.exitmark
            Exitmarks = read_file("exit.txt")
            for ext in Exitmarks:
                if mark == int(ext[1]):
                    landmark = ext[0]

    p = []#使用する駅
    for r in routes:
        p.append(r.route)

    route_gate = []
    if length == group.people:
        meet, kaisatu, one = Run(p, mark, dest) #待ち合わせの最適解
        kaisatuname = name(kaisatu)
        for n in range(len(route)):
            route_gate.extend([[route[n],kaisatuname[n]]])
        meet2 = point(meet)
        finalmeet = checker(meet2) #最終的に返す目的地の配列
        print("point利用"+str(finalmeet))
        meet = finalmeet
    params = {
        'landmark': landmark,
        'route': route,
        'group': group,
        'routes': routes,
        'meet': meet,
        'route_gate': route_gate,
        'length': length,
        'pathList_near': one,
    }
    return render(request, 'blog/map.html', params)



"""
mapページ内の追加ボタンを押した時
"""
def add_route(request, pk):
    errorM = "路線を選択してください"
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            route = form.save(commit="False")
            if route.route==-1:
                form = RouteForm()
                return render(request, 'blog/add_route.html', {'form': form, 'errorM': errorM})
            route.number = pk
            route.save()
            return redirect('map', pk=route.number)
        else:
            form = RouteForm()
            return render(request, 'blog/add_route.html', {'form': form, 'errorM': errorM})
    else:
        form = RouteForm()
        return render(request, 'blog/add_route.html', {'form': form, 'errorM': errorM})




def edit_route(request, pk):
    print(pk)
    return render(request, 'blog/index.html')
