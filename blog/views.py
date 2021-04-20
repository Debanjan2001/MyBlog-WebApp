from django.views.generic.base import TemplateView
from blog.forms import PostForm
from typing import Generic
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from blog.models import Post,Comment
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.core.paginator import Paginator


# Create your views here.

class LoginPage(LoginView):
    template_name = 'admin/login.html'

class LogoutPage(LogoutView):
    template_name = 'admin/logout.html'


class CreateNewPostView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    form_class = PostForm

    # def get_success_url(self):
    #     return reverse_lazy('blog:post_detail')
    # I have added get_absolute_url in Model . So this is not required anymore for redirect.

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = False).order_by('published_date').reverse()


class PostDetailPage(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    context_object_name = 'post'

    def get_queryset(self,pk): 
        post = get_object_or_404(Post,pk)
        post.comments = post.comments.all().order_by('created_date').reverse()
        return post;


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    context_object_name = 'post'
    redirect_field_name = 'blog/post_detail.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_confirm.html'
    success_url = reverse_lazy('blog:home')
    context_object_name = 'custom_object'

def publish_post_view(request,pk):
    post = get_object_or_404(Post,pk = pk)
    post.publish()
    return redirect('blog:home')

class DraftList(ListView):
    model = Post
    template_name = 'blog/draft.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('created_date')


class AuthorView(TemplateView):
    template_name = 'blog/author.html'



    



    

