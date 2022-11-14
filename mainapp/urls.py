from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main, name="main"),
    path('board/', views.board_post, name="board_post"),
    path('board/<int:pk>/', views.board_detail, name="board_detail"),

    path('comment_create/<int:pk>/', views.comment_create, name="comment_create"),
    path('comment_update/<int:pk>/', views.comment_update, name="comment_update"),
    path('comment_delete/<int:pk>/', views.comment_delete, name="comment_delete"),

    path('scrap/<int:pk>/', views.scrap, name="scrap"),
    # path('scrap_delete/<int:pk>/', views.scrap_delete, name="scrap_delete"),

    path('landing/', views.landing),
    
]