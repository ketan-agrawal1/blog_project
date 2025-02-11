from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView, PostLikeToggleView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('posts/<int:pk>/like/', PostLikeToggleView.as_view(), name='post-like-toggle'),
]
