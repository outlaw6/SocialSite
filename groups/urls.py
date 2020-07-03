# Groups urlspy():
from django.urls import url
from groups import views

app_name = groups

urlpatterns = [ path('', views.ListGroups.as_view(), name='all'),
                path('new/', views.CreateGroup.as_view(), name='create'),
                path('posts/in/<pk>'), views.SingleGroup.as_view(), name='single']
