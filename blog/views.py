from django.db.models.base import Model
from django.views.generic.base import TemplateView
from . forms import CommentForm, PostForm
from typing import Generic
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . models import Post,Comment
from django.contrib.auth.views import LoginView, LogoutView
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
    paginate_by = 3
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = False).order_by('published_date').reverse()


# class PostDetailView(DetailView):
#     template_name = 'blog/post_detail.html'
#     model = Post
#     context_object_name = 'post'

#     def get_queryset(self): 
#         print(self.request)
#         post = get_object_or_404(Post,pk = self.kwargs['pk'])
#         # post.comments = post.comments.all().order_by('created_date').reverse()
#         return post;

# Class based view is not comfortable in this case
def PostDetailView(request,pk):
    post = get_object_or_404(Post,pk= pk)
    context = {}
    context['post'] = post
    context['top_comments'] = post.comments.all().order_by('created_date').reverse()[:5]
    return render(request,'blog/post_detail.html',context)



class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    context_object_name = 'post'
    redirect_field_name = 'blog/post_detail.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete_confirm.html'
    success_url = reverse_lazy('blog:home')
    context_object_name = 'post'

def publish_post_view(request,pk):
    post = get_object_or_404(Post,pk = pk)
    post.publish()
    return redirect('blog:home')

class DraftList(ListView):
    paginate_by = 3
    model = Post
    template_name = 'blog/draft.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.filter(published_date__isnull = True).order_by('created_date').reverse()
        return posts


class AuthorView(TemplateView):
    template_name = 'blog/author.html'


def CreateCommentView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.publish()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

def CommentListView(request,pk):
    post = get_object_or_404(Post,pk = pk)
    context = {}
    paginator = Paginator(post.comments.all().order_by('created_date').reverse(), 5) # Show 5 comments per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request,'blog/comment_list.html',context=context)

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_delete_confirm.html'
    context_object_name = 'comment'
    
    def get_success_url(self):
        return reverse_lazy('blog:detail',kwargs = {'pk': self.object.post.pk })
    


    



    

