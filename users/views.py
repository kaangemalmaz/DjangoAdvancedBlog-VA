from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import *
from users.forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import *
from .forms import *
from posts.models import Post
from .models import UserProfile
# Create your views here.


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = '/users/login/'


class UserLogin(LoginView):
    template_name = 'users/login.html'


class UserLogout(LogoutView):
    template_name = 'users/login.html'


@method_decorator(login_required(login_url='users/login'),name='dispatch')
class UserProfileUpdateView(SuccessMessageMixin,UpdateView):
    template_name = 'users/profile-update.html'
    form_class = UserProfileForm
    model = UserProfile
    success_message = "Kullanıcı Profili başarılı bir şekilde güncellendi."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('users:update_profile',kwargs={'slug':self.object.slug})
    
    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseRedirect('/')
        return super(UserProfileUpdateView, self).get(request,*args,*kwargs)


@method_decorator(login_required(login_url='users/login'),name='dispatch')
class UserProfileView(ListView):
    template_name = 'users/my-profile.html'
    model = Post
    context_object_name = 'userposts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['userprofile']=UserProfile.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by('-id')



class UserPostView(ListView):
    template_name = 'users/user-posts.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(user=self.kwargs['pk'])


class UserListView(ListView):
    template_name = 'users/user-list.html'
    model = UserProfile
    context_object_name = 'users'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        return context
