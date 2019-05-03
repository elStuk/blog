from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response

from .models import Post
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import JsonResponse, request
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from blog.models import Post, Like
from .serializers import UserSerializer, GroupSerializer, PostSerializer, LikeSerializer
from rest_framework.renderers import JSONRenderer
from django.shortcuts import redirect


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = 5

def PostListViewFnc(request):
    user = User.objects.all()
    postsUser = Post.objects.order_by('-date_posted')

    likesDict = {}
    for onePost in postsUser:
        nrOfLIkes = Like.objects.filter(post=onePost, like_status=True).count()
        likesDict.update({onePost.id: nrOfLIkes})

    dislikesDict = {}
    for onePost in postsUser:
        nrOfLIkes = Like.objects.filter(post=onePost, like_status=False).count()
        dislikesDict.update({onePost.id: nrOfLIkes})

    context = {
        'posts': postsUser,
        'likesDict': likesDict,
        'dislikesDict': dislikesDict
    }
    return render(request, 'blog/home.html', context=context)


# class UserPostListView(ListView):
#     model = Post
#     template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     paginate_by = 5
#
#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Post.objects.filter(author=user).order_by('-date_posted')


def UserPostListViewFnc(request, username):
    user = get_object_or_404(User, username=username)
    postsUser = Post.objects.filter(author=user).order_by('-date_posted')

    likesDict = {}
    for onePost in postsUser:
        nrOfLIkes = Like.objects.filter(post=onePost, like_status=True).count()
        likesDict.update({onePost.id: nrOfLIkes})

    dislikesDict = {}
    for onePost in postsUser:
        nrOfLIkes = Like.objects.filter(post=onePost, like_status=False).count()
        dislikesDict.update({onePost.id: nrOfLIkes})

    context = {
        'posts': postsUser,
        'likes': Like.objects.filter(user=user, like_status=True).count(),
        'dislikes': Like.objects.filter(user=user, like_status=False).count(),
        'likesDict': likesDict,
        'dislikesDict': dislikesDict,
        'username': username
    }
    return render(request, 'blog/user_posts.html', context=context)


# class PostDetailView(DetailView):
#     model = Post


def PostDetailViewFnc(request, pk):
    post = Post.objects.filter(pk=pk)[0]
    likes = Like.objects.filter(post=post, like_status=True).count()
    dislikes = Like.objects.filter(post=post, like_status=False).count()

    context = {
        'post': post,
        'likes': likes,
        'dislikes': dislikes
    }
    return render(request, 'blog/post_detail.html', context=context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# update viwe
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def get_post(request):
    resonse = []
    for obj in Post.objects.all():
        resonse.append({
            'id': obj.id,
            "title": obj.title,
            "content": obj.content,
            "author": obj.author,
            'date_posted': obj.date_posted,
        })

    return JsonResponse({'response': resonse})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def PostPutLikeView(request, pk, username):
    post_instance = Post.objects.get(id=pk)
    user_instance = User.objects.get(username=username)

    if not Like.objects.filter(like_status=True, post=post_instance, user=user_instance).exists() \
            and not Like.objects.filter(like_status=False, post=post_instance, user=user_instance).exists():
        like = Like(like_status=True, post=post_instance, user=user_instance)
        like.save()

    return redirect('/post/' + str(post_instance.id))


def PostPutDislikeView(request, pk, username):
    post_instance = Post.objects.get(id=pk)
    user_instance = User.objects.get(username=username)

    if not Like.objects.filter(like_status=True, post=post_instance, user=user_instance).exists() \
            and not Like.objects.filter(like_status=False, post=post_instance, user=user_instance).exists():
        like = Like(like_status=False, post=post_instance, user=user_instance)
        like.save()

    return redirect('/post/' + str(post_instance.id))


class PostLikeView(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
