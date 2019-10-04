from django import forms
from .models import Post, Name, Group, Route

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
