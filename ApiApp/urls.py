from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'ApiApp'
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('tasks/', views.PostList.as_view()),
    path('tasks/<int:pk>/', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)