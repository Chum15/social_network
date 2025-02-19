from rest_framework import serializers
from posts.models import Post, Comment, Like


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'comments', 'created_at']
        read_only_fields = ['user',]


class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'photo', 'date']



class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializers(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField('like_count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'photo', 'date', 'comments', 'likes_count']
        read_only_fields = ['author',]

    def like_count(self, obj):
        return Like.objects.filter(post=obj).count()



class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['likes', 'post']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'comments', 'created_at','post']
        read_only_fields = ['user',]
