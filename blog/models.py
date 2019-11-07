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

NumberOfPeople = ((2,2),(3,3),(4,4),(5,5),)
DESTINATION = ((True,'あり'),(False,'なし'),)
Landmark = ((-1,'-------'),(100,'都庁'),(200,'新宿ピカデリー'),)
Route = ((1,'小田急小田原線'),(2,'都営新宿線'),(3,'東京メトロ丸ノ内線'),(4,'JR中央線'),(5,'JR埼京線'),(6,'JR総務線'),(7,'JR山の手線(外回り)'),(8,'JR山の手線(内回り)'),(9,'JR湘南新宿ライン'),(10,'京王線'),(11,'京王新線'),(0,'西武新宿線'),)

#Exit = FileRead("exit.txt");
#Landmark = FileRead("landmark.txt");
Exit = ((1,'出口１'),)

class Group(models.Model):
    number = models.CharField(max_length=100)
    people = models.IntegerField(choices=NumberOfPeople)
    destination = models.BooleanField(max_length=10,choices=DESTINATION)
    landmark = models.IntegerField(choices=Landmark,default=0)
    exitmark = models.IntegerField(choices=Exit,default=0)

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
    route = models.IntegerField(choices=Route)
    hour = models.CharField(max_length=10)
    minute = models.CharField(max_length=10)

    def __str__(self):
        return self.number
