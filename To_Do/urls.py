"""To_Do URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ToDoApp.views import TaskViewSet
from .yasg import urlpatterns as doc_urls

router = SimpleRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('ToDoApp/', include('ToDoApp.urls')),
    path('admin/', admin.site.urls),
    path('AuthorizationApp/', include('django.contrib.auth.urls')),
    path('AuthorizationApp/', include('AuthorizationApp.urls')),
    path('ApiApp/', include('ApiApp.urls')),
]
urlpatterns += doc_urls
urlpatterns += router.urls
