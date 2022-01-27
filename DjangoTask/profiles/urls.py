"""blog URL Configuration

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

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (

    ProfileDetailView, 
    ProfileListView,
    ProfileView,
    ProfileEditView,
    SkillCreateView,
    ProfileDeleteView

)
urlpatterns = [

    # home url
    path('',ProfileListView.as_view(),name='home'),
    # url to display profile page
    path('post/<int:pk>/',ProfileDetailView.as_view(),name='post-detail'),
    # url for profile form
    path('post/new/',ProfileView.as_view(),name='post-create'),
    # url for editing form
    path('post/edit/<id>/',ProfileEditView.as_view(),name='post-edit'),
    # url to create new skill
    path('post/create-skill/<id>/',SkillCreateView.as_view(),name='create-skill'),
    # delete url
    path('<pk>/delete/', ProfileDeleteView.as_view()),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
