"""
URL configuration for labs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from students.views import get_student_list, get_index, get_group_list, get_group_detail, get_student_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('group_list', get_group_list, name = 'group_list'),
    path('student_list', get_student_list, name = 'students_list'),
    path('', get_index, name = 'index'),
    path('group/detail', get_group_detail, name = 'group_detail'),
    path('students/detail', get_student_info, name = 'stud_info')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)