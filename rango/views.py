from django.shortcuts import render
from django.views.generic import View

from .models import Post

class SocialFeed(View):

    def get(self, request):
        post_objs = Post.objects.all()
        return render(request, 'index.html', context={'posts': post_objs})


