# Generated by Django 2.2.6 on 2019-10-22 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('people', models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (5, 5)])),
                ('destination', models.CharField(choices=[('あり', 'あり'), ('なし', 'なし')], max_length=10)),
                ('landmark', models.CharField(blank=True, choices=[('都庁', '都庁'), ('新宿ピカデリー', '新宿ピカデリー')], max_length=20)),
                ('exitmark', models.CharField(blank=True, choices=[('出口1', '出口１')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('route', models.CharField(choices=[('中央線', '中央線'), ('山の手線', '山の手線'), ('西武新宿線', '西武新宿線')], max_length=20)),
            ],
        ),
    ]
