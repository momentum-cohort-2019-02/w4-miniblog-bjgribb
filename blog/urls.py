from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogpost/', views.BlogPostListView.as_view(), name='blogpost'),
    path('blogpost/<int:pk>', views.BlogPostDetailView.as_view(), name='blogpost-detail')
]
