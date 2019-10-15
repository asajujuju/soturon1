from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Group, Route
from .forms import PostForm, NameForm, GroupForm, RouteForm

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})



"""
8000にアクセスした時
index.htmlを表示する
"""
def index(request):
    return render(request, 'blog/index.html')



"""
1. index.htmlの待ち合わせボタンを押した時
   else文を実行してselect.htmlを表示する
2. select.htmlのSaveボタンを押した時
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

def map(request, pk):
    group = get_object_or_404(Group, pk=pk)
    routes = Route.objects.filter(number=pk)
    return render(request, 'blog/map.html', {'group': group, 'routes': routes})

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
