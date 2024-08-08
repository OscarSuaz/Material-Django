from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView



from .models import Post

class PostListView(PermissionRequiredMixin,ListView):
    permission_required="publicaciones.view_post"
    template_name="post.html"
    model=Post

