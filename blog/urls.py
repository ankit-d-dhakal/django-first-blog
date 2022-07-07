from django.urls import path

from . views import index, single, create

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', single, name='single_blog_page'),
    path('create/', create, name='create_blog_page'),
    # path('random-blog/', random_blog, name='random_blog_page'),
]