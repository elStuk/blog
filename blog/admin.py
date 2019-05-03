from django.contrib import admin
<<<<<<< HEAD
from . models import Post, Like

admin.site.register(Post)
admin.site.register(Like)
=======
from .models import Post, Like

admin.site.register(Post)


class LikeList(admin.ModelAdmin):
    list_display = ('post', 'like_status', 'user')


admin.site.register(Like, LikeList)
>>>>>>> 1273c3fe2dcbd1f921a87372a08bf8e4f63afa7a
