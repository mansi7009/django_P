from django.urls import path,include
from members.views import index
from .views import *
urlpatterns = [
    path('',display_laptops,name = 'display_laptops'),
    path('display_laptops',display_laptops,name = 'display_laptops'),   #path url ka yha set hoga nd display_laptops function call hga views mei 
    path('display_desktops',display_desktops,name = 'display_desktops'),   
    path('display_mobiles',display_mobiles,name = 'display_mobiles'),
    path('add_laptop',add_laptop,name = 'add_laptop'),
    path('add_desktop',add_desktop,name = 'add_desktop'),
    path('add_mobile',add_mobile,name = 'add_mobile'),

    path('edit_laptop/<int:pk>/', edit_laptop,name = 'edit_laptop'),
    path('edit_desktop/<int:pk>/', edit_desktop,name = 'edit_desktop'),
    path('edit_mobile/<int:pk>/', edit_mobile,name = 'edit_mobile'),

    path('delete_laptop/<int:pk>/', delete_laptop,name = 'delete_laptop'),
    path('delete_desktop/<int:pk>/', delete_desktop,name = 'delete_desktop'),
    path('delete_mobile/<int:pk>/', delete_mobile,name = 'delete_mobile'),





]
