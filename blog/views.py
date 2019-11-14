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
select.htmlやadd.htmlでSaveボタンを押した時のリダイレクト先。
Groupテーブル、Routeテーブルから必要なオブジェクトを取り出し、
そのオブジェクトをmap.htmlに与えて表示させる
"""
def map(request, pk):
    group = get_object_or_404(Group, pk=pk)
    routes = Route.objects.filter(number=pk)
    cafes = Cafe.objects.all()
    dest = False #目的地の有無
    mark = 0 #ランドマークor出口のノード番号
    if group.destination:
        dest = True
        if group.landmark != -1:
            mark = group.landmark
        else:
            mark = group.exitmark
    meet = Run([220, 217], mark, dest) #待ち合わせの最適解
    return render(request, 'blog/map.html', {'group': group, 'routes': routes, 'meet': meet, 'cafes': cafes})



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
