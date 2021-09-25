from django.urls import path
from .views import UserRegisterView

app_name = 'AuthorizationApp'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),

]
