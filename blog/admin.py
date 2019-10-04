from django.contrib import admin

# Register your models here.
from .models import Post, Cafe, Name, Group, Route

admin.site.register(Post)
admin.site.register(Cafe)
admin.site.register(Name)
admin.site.register(Group)
admin.site.register(Route)
