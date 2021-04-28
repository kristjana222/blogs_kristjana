from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('login', views.login, name='login'),
    path('<int:blogs_id>', views.comment_page, name='comment_page'),
    path('listo/<int:blogs_id>', views.comment_page, name='comment_page1'),
    path('blogger_list', views.blogger_list, name='blogger_list'),
    path('blog/<int:blogger_id>', views.blogger_bio, name='blogger_bio'),
    path('blog_bio/<int:blogger_id>', views.blogger_bio, name='blogger_bio'),
    path('add_comment', views.add_comment, name='add_comment'),
    path('register', views.register, name='register'),
    path('new_post', views.new_post, name='new_post'),
    path('krijo_coment', views.krijo_coment, name='krijo_koment'),
    path('create_blog', views.create_new_blog, name='krijo_blog'),
    path('add_post', views.add_post),
    path('krijo_coment', views.krijo_coment)



]
