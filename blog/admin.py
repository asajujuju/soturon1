from django.contrib import admin

# Register your models here.
from .models import Cafe, Group, Route

admin.site.register(Cafe)
admin.site.register(Group)
admin.site.register(Route)
