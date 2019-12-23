# Generated by Django 2.2.7 on 2019-12-19 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20191219_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='landmarknumber',
        ),
        migrations.AlterField(
            model_name='group',
            name='landmark',
            field=models.IntegerField(choices=[[-1, '--------'], [539, '新宿サザンテラス'], [245, '高島屋'], [522, '新宿郵便局'], [522, '京王プラザホテル'], [522, '新宿中央公園'], [522, '東京都庁'], [611, '新宿ワシントンホテル'], [606, '小田急サザンタワー'], [243, '新宿御苑'], [245, '高島屋タイムズスクエア'], [212, 'ビックロ'], [43, 'ルミネエスト'], [539, 'ルミネ２'], [402, '小田急百貨店本館'], [539, '京王百貨店'], [516, '工学院大学'], [539, 'ルミネ１'], [425, '新宿エルタワー'], [208, '紀伊国屋ビル'], [230, '花園神社'], [322, 'スタジオアルタ'], [26, '小田急ハルク'], [208, '新宿ピカデリー'], [214, '伊勢丹'], [108, 'TOHOシネマズ新宿'], [228, '新宿バルト９'], [539, 'ルミネtheよしもと'], [215, '新宿マルイ本館']], default=0),
        ),
    ]
