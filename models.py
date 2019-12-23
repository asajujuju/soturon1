import os
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

def FileReads(t):
     #ファイルを読み込む
    file_data = open(t, "r")
    firstline = True
    #読み込んだファイルを1行ずつ表示
    landmark = []
    for line in file_data:
        data = line.split(' ')#空白文字で区切る
        userval = str(data[0])#データベースに入れる値
        dbval = str(data[1])#ユーザーが見る値
        landmark.append([dbval, userval])#出口
    #開いたファイルを閉じる
    file_data.close()
    return(landmark)

NumberOfPeople = ((2,2),(3,3),(4,4),(5,5),)
DESTINATION = ((True,'あり'),(False,'なし'),)
Exit = FileRead("exit.txt")
#Exit = FileRead("/home/nanako/nanako.pythonanywhere.com/exit.txt")
Landmark = FileReads("landmarkafter.txt")
#Landmark = FileRead("/home/nanako/nanako.pythonanywhere.com/landmark.txt")
Landmarkn = FileRead("landmark.txt")

class Group(models.Model):
    people = models.IntegerField(choices=NumberOfPeople)
    destination = models.BooleanField(choices=DESTINATION, default=False)
#文字を格納する
    landmark = models.CharField(max_length=100,choices=Landmark)
    exitmark = models.IntegerField(choices=Exit,default=0)
    landmarknumber = models.IntegerField(choices=Landmarkn,default=0)
    
    
    def __str__(self):
        return str(self.pk)

"""
個人が利用する路線、時間の情報
   number (int) : グループ番号
   route (char) : 駅到着時の路線
   hour (char) : 到着時
   minute (char) : 到着分
"""

Route = FileRead("route.txt")
#Route = FileRead("/home/nanako/nanako.pythonanywhere.com/route.txt");
class Route(models.Model):
    number = models.CharField(max_length=100)
    route = models.IntegerField(choices=Route)

    def __str__(self):
        return self.number