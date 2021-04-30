from django.conf.urls import url
from api_stage import views

urlpatterns = [
    url(r'^api/v1/users$', views.manage_users),
    url(r'^api/v1/users/(?P<pk>[0-9]+)$', views.users_detail),
    url(r'^api/v1/profile$', views.manage_profiles),
    url(r'^api/v1/profile/(?P<pk>[0-9]+)$', views.profiles_detail),
    url(r'^api/v1/posts$', views.manage_posts),
    url(r'^api/v1/posts/(?P<pk>[0-9]+)$', views.posts_detail),
    url(r'^api/v1/upload$', views.file_store),
    url(r'^api/v1/login', views.login_view),
    url(r'^api/v1/comments$', views.manage_comments),
    url(r'^api/v1/comments/(?P<pk>[0-9]+)$', views.comments_detail),
]
