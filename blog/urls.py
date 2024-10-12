from django.urls import path
from .views import PostListView, PostDetailView,PostCreateView,PostDeleteView
from .views import PostUpdateView
urlpatterns = [ 
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/create/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    ]               


# <button class="btn btn-secondary rounded-pill px-3" type="button">Secondary</button>