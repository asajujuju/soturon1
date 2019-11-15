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
#Exit = FileRead("nanana3.pythonanywhere.com/exit.txt");
#Landmark = FileRead("nanana3.pythonanywhere.com/landmark.txt");
Exit = FileRead("blog/static/text/exit.txt");
Landmark = FileRead("blog/static/text/landmark.txt");

class Group(models.Model):
    people = models.IntegerField(choices=NumberOfPeople)
    destination = models.BooleanField(choices=DESTINATION, default=False)
    landmark = models.IntegerField(choices=Landmark,default=0)
    exitmark = models.IntegerField(choices=Exit,default=0)

    def __str__(self):
        return str(self.pk)

"""
個人が利用する路線、時間の情報
   number (int) : グループ番号
   route (char) : 駅到着時の路線
   hour (char) : 到着時
   minute (char) : 到着分
"""

#Route = FileRead("nanana3.pythonanywhere.com/route.txt");
Route = FileRead("blog/static/text/route.txt");
class Route(models.Model):
    number = models.CharField(max_length=100)
    route = models.IntegerField(choices=Route)

    def __str__(self):
        return self.number
