from django.urls import path
from . import views
from .views import (PostListView,
                    PostCreateView, PostUpdateView,
                    PostDeleteView, UserPostListViewFnc,
                    PostDetailViewFnc)
from blog import views as u_w
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListViewFnc, name='user-posts'), #UserPostListView.as_view()
    path('post/<int:pk>/', PostDetailViewFnc, name='post-detail'), #PostDetailView.as_view()
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/like/<str:username>', u_w.PostPutLikeView, name='post-like'),
    path('post/<int:pk>/dislike/<str:username>', u_w.PostPutDislikeView, name='post-dislike'),
    path('about/', views.about, name='blog-about'),
]
