from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog.models import Post, Like



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'date_posted', 'author')


<<<<<<< HEAD
class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

=======
# class LikeSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required=False)
#
#     class Meta:
#         model = Post
#         fields = '__all__'
#         read_only_fields = ('post',)


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="like-detail")

    class Meta:
        model = Like
        fields = '__all__'
>>>>>>> 1273c3fe2dcbd1f921a87372a08bf8e4f63afa7a
