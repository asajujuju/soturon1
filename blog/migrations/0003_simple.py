# Generated by Django 2.0.13 on 2019-10-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_cafe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Simple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]