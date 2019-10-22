from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select/', views.select, name='select'),
    path('map/<int:pk>', views.map, name='map'),
    path('add/<int:pk>', views.add_route, name='add_route'),
]
