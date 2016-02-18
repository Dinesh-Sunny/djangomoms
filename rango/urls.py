from django.conf.urls import url

from .views import SocialFeed

urlpatterns = [
    url(r'hello/', SocialFeed.as_view(), name='social_feed')
]