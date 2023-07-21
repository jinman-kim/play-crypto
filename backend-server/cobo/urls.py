# cobo/urls.py
from django.urls import path
from . import views

app_name = 'cobo'

# cobo/urls.py
urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('post_create', views.post_create, name='post_create'), 
    path('post_detail', views.post_detail, name='post_detail'),  # 새 게시물 작성 페이지 URL
]
