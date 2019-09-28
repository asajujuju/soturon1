from django.db import models
from django.utils import timezone

#�������疳����
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

#�����܂Ł�

class Meeting(models.Model):
    #PEOPLE_CHOICE = (
    #('2','2�l'),
    #('3','3�l'),
    #('4','4�l'),
    #('5','5�l'),
    #)
    #people = models.CharField(max_length=20)
    destination = models.IntegerField()
    #landmark = models.CharField(max_length=30)
    #exitmark = models.CharField(max_length=30)

    def _str_(self):
        return self.people
