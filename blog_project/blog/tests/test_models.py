import pytest
from django.contrib.auth.models import User
from blog.models import Post, Comment

@pytest.mark.django_db
def test_post_creation():
    user = User.objects.create_user(username='testuser', password='12345')
    post = Post.objects.create(title='Test Post', content='Test Content', author=user)
    assert post.title == 'Test Post'
    assert post.content == 'Test Content'
    assert post.author.username == 'testuser'

@pytest.mark.django_db
def test_comment_creation():
    user = User.objects.create_user(username='testuser', password='12345')
    post = Post.objects.create(title='Test Post', content='Test Content', author=user)
    comment = Comment.objects.create(post=post, author='Commenter', text='Test Comment')
    assert comment.post.title == 'Test Post'
    assert comment.author == 'Commenter'
    assert comment.text == 'Test Comment'
