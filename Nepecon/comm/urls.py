from django.urls import path
from comm import views

urlpatterns = [
    path('', views.PostListView.as_view(), name = 'post_list'),
    path('about/', views.AboutView.as_view(), name = 'about'),
    path('post/(?P<pk>\d+)', views.PostDetailView.as_view(), name = 'post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name = 'post_new'),
    path('post/(?P<pk>\d+)/edit', views.PostUpdateView.as_view(), name = 'post_update'),
    path('post/(?P<pk>\d+)/delete/', views.DeleteView.as_view(), name = 'post_delete'),
    path('drafts/', views.DraftListView.as_view(), name ='post_draft'),
    path('post/(?P<pk>\d+)/comment', views.add_comment_to_post, name = 'add_comment'),
    path('comments/(?P<pk>\d+)/approve/', views.comment_approve, name = 'comment_approve'),
    path('comments/(?P<pk>\d+)/remove/', views.comment_remove, name = 'comment_remove'),
    path('post/(?P<pk>\d+)/publish/', views.post_publish, name= 'post_publish'),
]
