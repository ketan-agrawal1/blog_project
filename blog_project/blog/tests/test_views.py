import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from blog.models import Post, Comment
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='12345')

@pytest.fixture
def user_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@pytest.fixture
def post(user):
    return Post.objects.create(title='Test Post', content='Test Content', author=user)

@pytest.mark.django_db
def test_post_list(api_client):
    response = api_client.get('/api/posts/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_post_create(api_client, user_token):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_token['access'])
    response = api_client.post('/api/posts/', {'title': 'New Post', 'content': 'New Content', 'author': 1})
    assert response.status_code == 201

@pytest.mark.django_db
def test_post_detail(api_client, post):
    response = api_client.get(f'/api/posts/{post.id}/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_post_update(api_client, post, user_token):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_token['access'])
    response = api_client.put(f'/api/posts/{post.id}/', {'title': 'Updated Post', 'content': 'Updated Content', 'author': post.author.id})
    assert response.status_code == 200

@pytest.mark.django_db
def test_post_delete(api_client, post, user_token):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_token['access'])
    response = api_client.delete(f'/api/posts/{post.id}/')
    assert response.status_code == 204

@pytest.mark.django_db
def test_comment_list(api_client, post):
    response = api_client.get(f'/api/posts/{post.id}/comments/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_comment_create(api_client, post, user_token):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_token['access'])
    response = api_client.post(f'/api/posts/{post.id}/comments/', {'post': post.id, 'author': 'Commenter', 'text': 'New Comment'})
    assert response.status_code == 201

@pytest.mark.django_db
def test_post_like(api_client, post, user_token):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_token['access'])
    response = api_client.post(f'/api/posts/{post.id}/like/')
    assert response.status_code == 200
    assert response.data['liked'] == True
    assert response.data['like_count'] == 1

@pytest.mark.django_db
def test_post_unlike(api_client, post, user_token):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_token['access'])
    # First, like the post
    api_client.post(f'/api/posts/{post.id}/like/')
    # Then, unlike the post
    response = api_client.post(f'/api/posts/{post.id}/like/')
    assert response.status_code == 200
    assert response.data['liked'] == False
    assert response.data['like_count'] == 0
