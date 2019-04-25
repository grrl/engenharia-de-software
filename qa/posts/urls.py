from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('post/', views.post, name='post'),
]





