from django.http import HttpResponse
from django.views.generic import View


class SocialFeed(View):

    def get(self, request):
        
        return HttpResponse('Hello How are you?')
