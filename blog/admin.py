from django.contrib import admin
from .models import Post, Like

admin.site.register(Post)
admin.site.register(Like)
from .models import Post, Like

admin.site.register(Post)


class LikeList(admin.ModelAdmin):
    list_display = ('post', 'like_status', 'user')


admin.site.register(Like, LikeList)
