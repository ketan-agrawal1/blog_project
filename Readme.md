# Django Blog Application

## Overview

This is a simple blog application built using Django and Django REST Framework, featuring basic CRUD functionalities for `Post` and `Comment` models. The application also supports token-based authentication using `djangorestframework-simplejwt` and allows users to like/unlike posts.

## Features

- CRUD operations for posts and comments.
- Token-based authentication.
- Like/Unlike functionality for posts.
- JSON responses for all API endpoints.
- Basic unit tests using `pytest`.

## Setup Instructions

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST Framework
- `djangorestframework-simplejwt`
- `pytest` and `pytest-django`

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ketan-agrawal1/blog_project.git
    cd blog_project
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

### API Endpoints

1. **Post Endpoints:**

    - List all posts:
        ```
        GET /api/posts/
        ```
    - Create a new post (authenticated users only):
        ```
        POST /api/posts/
        ```
    - Retrieve a specific post:
        ```
        GET /api/posts/{id}/
        ```
    - Update a post (authenticated users only):
        ```
        PUT /api/posts/{id}/
        ```
    - Delete a post (authenticated users only):
        ```
        DELETE /api/posts/{id}/
        ```

2. **Comment Endpoints:**

    - List all comments for a post:
        ```
        GET /api/posts/{post_id}/comments/
        ```
    - Create a new comment for a post (authenticated users only):
        ```
        POST /api/posts/{post_id}/comments/
        ```

3. **Like/Unlike Post Endpoint:**

    - Like/Unlike a post (authenticated users only):
        ```
        POST /api/posts/{id}/like/
        ```

4. **Authentication Endpoints:**

    - Obtain token pair (access and refresh tokens):
        ```
        POST /api/token/
        ```
    - Refresh access token:
        ```
        POST /api/token/refresh/
        ```

### Authentication

To interact with the protected endpoints, you need to authenticate using JWT. Follow these steps:

1. Obtain a token pair (access and refresh tokens) by sending a POST request with your username and password to `/api/token/`.

    ```bash
    curl -X POST -d "username=yourusername&password=yourpassword" http://localhost:8000/api/token/
    ```

2. Include the access token in the `Authorization` header for subsequent requests:

    ```
    Authorization: Bearer <your_access_token>
    ```

3. Refresh the access token by sending a POST request with your refresh token to `/api/token/refresh/`.

    ```bash
    curl -X POST -d "refresh=<your_refresh_token>" http://localhost:8000/api/token/refresh/
    ```

### Running Tests

To run the unit tests, use the following command:

```bash
pytest
