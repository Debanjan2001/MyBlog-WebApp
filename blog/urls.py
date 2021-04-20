from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.PostListView.as_view(),name = 'home'),
    path('post/create/',views.CreateNewPostView.as_view(),name = 'create'),
    path('login/',views.LoginPage.as_view(), name = 'login'),
    path('logout/',views.LogoutPage.as_view(),name = 'logout'),
    path('post/<int:pk>/',views.PostDetailPage.as_view(),name= 'detail'),
    path('drafts/',views.DraftList.as_view(),name = 'drafts'),
    path('post/update/<int:pk>',views.PostUpdateView.as_view(),name = 'update'),
    path('post/delete/<int:pk>',views.PostDeleteView.as_view(),name = 'delete'),
    path('post/publish/<int:pk>',views.publish_post_view,name='publish'),
    path('about/',views.AuthorView.as_view(),name = 'about'),

]
