from django import forms
from .models import Post, Name, Group, Route
<<<<<<< HEAD

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

"""
        number = forms.CharField(
        label='グループ番号',
        max_length=100,
        required=True,
        )

        people = forms.IntegerField(
        label='人数',
        required=True,
        )

        destination = forms.ChoiceField(
        label='目的地',
        widget=forms.Select,
        choices=DESTINATION,
        required=True,
        )

        landmark = forms.CharField(
        label='ランドマーク',
        max_length=50,
        required=True,
        )

        exitmark = forms.CharField(
        label='出口',
        required=True,
        )
"""
    #class Meta:
        #model = Group
        #fields = ('number', 'people', 'destination', 'landmark', 'exitmark',)

class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = ('route', 'hour', 'minute',)
