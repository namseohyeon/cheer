from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main, name="main"),
    path('board/', views.board_post, name="board_post"),
    path('board/<int:pk>/', views.board_detail, name="board_detail"),
    path('mainapp/category/<str:slug>/', views.category_page),
    path('mainapp/tag/<str:name>/', views.tag_page, name="tag_page"),
    path('comment_create/<int:pk>/', views.comment_create, name="comment_create"),
    path('comment_update/<int:pk>/', views.comment_update, name="comment_update"),
    path('comment_delete/<int:pk>/', views.comment_delete, name="comment_delete"),
    path('board/search/', views.search, name='search'),
    path('scrap/<int:pk>/', views.scrap, name="scrap"),
    # path('scrap_delete/<int:pk>/', views.scrap_delete, name="scrap_delete"),
    
    path('vote/', views.vote, name="vote"),
    path('vote_to/', views.vote_to, name="vote_to"),
    path('vote_result/', views.vote_result, name="vote_result"),

    path('landing/', views.landing),
    path('about/', views.about),
]
