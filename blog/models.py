from django.db import models
from django.utils import timezone

#チュートリアル用のデータベース
#後で削除する
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


#formとmodelの接続テスト用
class Name(models.Model):
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

#
#↓ここからダンジョンで使う
#

#新宿駅周辺のカフェ、レストランの情報
class Cafe(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

"""
待ち合わせのためのグループ情報
   number (int) : グループ番号
   people (int) : グループの人数
   destination (char) : 目的地の有無
   landmark (char) : ランドマーク(目的地)情報
   exitmark (char) : 出口(目的地)情報
"""
NumberOfPeople = ((1,1),(2,2),(3,3),(4,4),(5,5),)

Landmark = (('都庁','都庁'),)

Exit = (('出口1','出口１'),)


class Group(models.Model):
    number = models.CharField(max_length=100)
    #people = models.IntegerField()
    people = models.ChoiceField(lavel='人数', widget=forms.Select, choices=NumberOfPeople, required=True,)
    #destination = models.CharField(max_length=10)
    destination = models.CharField(widget=forms.Select,)
    #landmark = models.CharField(max_length=20)
    landmark = models.ChoiceField(lavel='ランドマーク', widget=forms.Select, choices=Landmark, required=True,)
    #exitmark = models.CharField(max_length=20)
    exitmark = models.ChoiceField(lavel='出口', widget=forms.Select, choices=Exit, required=True,)

    def __str__(self):
        return self.number

"""
個人が利用する路線、時間の情報
   number (int) : グループ番号
   route (char) : 駅到着時の路線
   hour (char) : 到着時
   minute (char) : 到着分
"""
class Route(models.Model):
    number = models.CharField(max_length=100)
    route = models.CharField(max_length=20)
    hour = models.CharField(max_length=5)
    minute = models.CharField(max_length=5)

    def __str__(self):
        return self.number
