from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_room),
    path('all/', views.get_all_rooms),
    path('<str:id>/', views.get_room),
    path('delete/<str:id>/', views.delete_room),
    path('message/<str:id>/', views.get_message),
    path('message/delete/<str:id>/', views.delete_message),
    path('<str:room_id>/message/', views.create_message),
    path('<str:room_id>/message/all/', views.get_room_messages),
]