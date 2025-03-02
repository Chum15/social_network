from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet
from posts.models import Post, Comment, Like
from posts.permissions import IsOwnerOrReadOnly
from posts.serializers import PostSerializer, CommentSerializer, LikeSerializer



class PostViwSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class CommentViwSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class LikeViwSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(users=self.request.user)
