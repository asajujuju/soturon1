# Generated by Django 2.0.13 on 2019-10-22 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20191022_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='exitmark',
            field=models.IntegerField(blank=True, choices=[(300, '出口１')]),
        ),
        migrations.AlterField(
            model_name='group',
            name='landmark',
            field=models.IntegerField(blank=True, choices=[(100, '都庁'), (200, '新宿ピカデリー')]),
        ),
    ]