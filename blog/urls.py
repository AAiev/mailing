from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, HomeView

app_name = BlogConfig.name

urlpatterns = [
    path('', HomeView.as_view(template_name='blog/home.html'), name='home'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<str:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_form'),
    path('blog/update/<str:slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<str:slug>/', BlogDeleteView.as_view(), name='blog_delete'),
]
