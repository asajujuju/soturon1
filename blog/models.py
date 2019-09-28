from django.db import models
from django.utils import timezone

#ここから無視↓
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

    def _str_(self):
        return self.title

#ここまで↑

class Meeting(models.Model):
    #PEOPLE_CHOICE = (
    #('2','2人'),
    #('3','3人'),
    #('4','4人'),
    #('5','5人'),
    #)
    #people = models.CharField(max_length=20)
    destination = models.IntegerField()
    #landmark = models.CharField(max_length=30)
    #exitmark = models.CharField(max_length=30)

    def _str_(self):
        return self.people
