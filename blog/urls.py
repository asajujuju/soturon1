from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('select/', views.select, name='select'),
    path('map/<int:pk>', views.map, name='map'),
    path('add/<int:pk>', views.add_route, name='add_route'),
    path('edit/<int:pk>', views.edit_route, name='edit_route'),
]
