from django.urls import path
from . import views

urlpatterns = [
	path('websocket-test/', views.websocket_test_view, name='websocket_test'),
	path('', views.index, name='index'),
	path('chat/<str:room_name>/', views.room, name='room'),
]
