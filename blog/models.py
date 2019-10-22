from django.db import models
from django.utils import timezone

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

NumberOfPeople = ((2,2),(3,3),(4,4),(5,5),)
DESTINATION = (('あり','あり'),('なし','なし'),)
Landmark = (('100','都庁'),('200','新宿ピカデリー'),)
Exit = (('300','出口１'),)
Route = (('1','小田急小田原線'),('2','都営新宿線'),('3','東京メトロ丸ノ内線'),('4','JR中央線'),('5','JR埼京線'),('6','JR総務線'),('7','JR山の手線(外回り)'),('8','JR山の手線(内回り)'),('9','JR湘南新宿ライン'),('10','京王線'),('11','京王新線'),('12','西武新宿線'),)

class Group(models.Model):
    number = models.CharField(max_length=100)
    people = models.IntegerField(choices=NumberOfPeople)
    destination = models.CharField(max_length=10,choices=DESTINATION)
    landmark = models.CharField(max_length=20,choices=Landmark,blank=True)
    exitmark = models.CharField(max_length=20,choices=Exit,blank=True)

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
    route = models.CharField(max_length=20,choices=Route)
    hour = models.CharField(max_length=10)
    minute = models.CharField(max_length=10)

    def __str__(self):
        return self.number
