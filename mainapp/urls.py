from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main, name="main"),
    path('board/', views.board_post, name="board_post"),
    path('board/<int:pk>/', views.board_detail, name="board_detail"),
    ] 