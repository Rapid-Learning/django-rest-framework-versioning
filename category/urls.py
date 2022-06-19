from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from category import views

urlpatterns = [
    re_path(r'^$', views.category_list, name='category-list'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.category_detail, name='category-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)

app_name = 'category'
