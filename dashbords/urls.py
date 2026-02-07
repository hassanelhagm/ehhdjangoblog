
from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashbord, name='dashbord'),  # Dashboard home page
    #category management urls (crud)
    path('categories/', views.categories, name='categories'),  # Category management page
    path('categories/add/', views.add_category, name='add_category'),  # Add new category
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),

    #posts management urls (crud)
    path('posts/', views.posts, name='posts'),  # Post management page
    path('posts/add/', views.add_post, name='add_post'),  # Add new post
    path('posts/edit/<int:pk>/', views.edit_post, name='edit_post'),  # Edit existing post
    path('posts/delete/<int:pk>/', views.delete_post, name='delete_post'),  # Delete existing post

    #users management urls (crud)
    path('users/', views.users, name='users'),  # User management page
    path('users/add/', views.add_user, name='add_user'),  # Add new user
    path('users/edit/<int:pk>/', views.edit_user, name='edit_user'),  # Edit existing user
    path('users/delete/<int:pk>/', views.delete_user, name='delete_user'),  # Delete existing user
    


  
]