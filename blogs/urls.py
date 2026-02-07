from django.urls import path
from . import views

urlpatterns = [

   
path('<int:category_id>/', views.posts_by_categoryId, name='posts_by_categoryId'),

]