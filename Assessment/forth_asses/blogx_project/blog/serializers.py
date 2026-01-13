from rest_framework import serializers
from .models import Post, Comment, Category, Like

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_at']
        read_only_fields = ['post'] # Post is handled by the URL or context

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    likes_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'category', 'title', 'content', 'cover_image', 'created_at', 'likes_count', 'comments']

    def get_likes_count(self, obj):
        return obj.likes.count()