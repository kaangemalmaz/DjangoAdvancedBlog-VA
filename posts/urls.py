from django.urls import path
from posts.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:pk>/<slug:slug>', PostDetailView.as_view(), name='detail'),
    path('category/<int:pk>/<slug:slug>', CategoryDetail.as_view(), name='category_detail'),
    path('tag/<slug:slug>', TagDetail.as_view(), name='tag_detail'),
    path('posts-create/', CreatePostView.as_view(), name='create_post'),
    path('posts-update/<int:pk>/<slug:slug>', UpdatePostView.as_view(), name='update_post'),
    path('posts-delete/<int:pk>/<slug:slug>', PostDeleteView.as_view(), name='delete_post'),
    path('search/', SearchPost.as_view(), name='search'),
]


