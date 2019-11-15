from django import forms
from .models import Group, Route

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('people', 'destination', 'landmark', 'exitmark',)

class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = ('route',)
