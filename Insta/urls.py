"""InstaJZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from Insta.views import (HelloWorld, EditProfile, ExploreView, PostCreateView,
                         PostDeleteView, PostDetailView, PostView,
                         PostUpdateView, SignUp, UserProfile, addComment,
                         addLike, toggleFollow)

urlpatterns = [
    path('helloworld/', HelloWorld.as_view(), name='helloworld'),
    path('', PostView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('post/new/', PostCreateView.as_view(), name='make_post'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('like', addLike, name='addLike'),
    path('user_profile/<int:pk>/', UserProfile.as_view(), name='profile'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
    path('togglefollow', toggleFollow, name='togglefollow'),
    path('comment', addComment, name='addComment'),
    path('explore', ExploreView.as_view(), name='explore'),
    
]
