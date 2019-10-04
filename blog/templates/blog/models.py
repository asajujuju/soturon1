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
class Group(models.Model):
    number = models.CharField(max_length=100)
    people = models.IntegerField()
    destination = models.CharField(max_length=10)
    landmark = models.CharField(max_length=20)
    exitmark = models.CharField(max_length=20)

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
