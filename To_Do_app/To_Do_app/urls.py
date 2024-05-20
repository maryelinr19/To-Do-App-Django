"""
URL configuration for To_Do_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from tasks import views as task_views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_views.task_list, name='task_list'),
    path('tasks/create/', task_views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', task_views.task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', task_views.task_delete, name='task_delete'),
    path('accounts/register/', account_views.register, name='register'),
    path('accounts/login/', account_views.login_view, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]
