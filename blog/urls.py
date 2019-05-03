from django.urls import path
from . import views
from .views import (PostListView, PostDetailView,
                    PostCreateView, PostUpdateView,
                    PostDeleteView, UserPostListView)
from blog import views as u_w
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/like/', u_w.PostLikeView, name='post-like'),
    path('post/<int:pk>/dislike/', u_w.PostDislikeView, name='post-dislike'),
    path('about/', views.about, name='blog-about'),
]
