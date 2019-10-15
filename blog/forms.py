from django import forms
from .models import Post, Name, Group, Route

NumberOfPeople = ((1,1),(2,2),(3,3),(4,4),(5,5),)

DESTINATION = (('あり','あり'),('なし','なし'),)

Landmark = (('都庁','都庁'),)

Exit = (('出口1','出口１'),)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class NameForm(forms.ModelForm):

    class Meta:
        model = Name
        fields = ('number', 'name',)

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('number', 'people', 'destination', 'landmark', 'exitmark',)

class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = ('route', 'hour', 'minute',)
