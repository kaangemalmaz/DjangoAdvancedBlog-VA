from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import *
from django.contrib.auth import views as authViews

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('password-change/', authViews.PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', authViews.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('update-profile/<slug:slug>', UserProfileUpdateView.as_view(), name='update_profile'),
    path('myprofile/', UserProfileView.as_view(), name='myprofile'),
    path('<int:pk>/', UserPostView.as_view(), name='user_posts'),
    path('', UserListView.as_view(), name='userlist'),
]