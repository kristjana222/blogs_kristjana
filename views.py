from django.shortcuts import render, redirect, reverse, resolve_url
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import urls
from django.contrib import messages
from .models import Blogger, Blogs, CommenterUser, Comment, AbstractUser, auth


def index(request):
    return render(request, 'home_page.html')


def blogs1(request):
    return render(request, 'blogger_bio.html')


def new(request):
    blogs = Blogs.objects.order_by('date_post')
    return render(request, 'blog_list.html', {'blog': blogs})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('add_comment')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        is_blogger = request.POST['blogger']
        comment_u = CommenterUser.objects.create_user(first_name=firstname, last_name=lastname, username=username,
                                                      password=password, is_blogger=is_blogger)
        comment_u.save()
        return redirect('login')
    else:
        return render(request, 'registration.html')


def comment_page(request, blogs_id):
    blog1 = Blogs.objects.get(id=blogs_id)
    user_com = blog1.blog_set.order_by('-date_postc')
    return render(request, 'comment_page.html', {'blog1': blog1, 'user': user_com})


def blogger_list(request):
    bloger_list = Blogger.objects.all()

    #dt = datatime.nowI()
    # user=request.user
    return render(request, 'bloger_list.html', {'bloger_list': bloger_list})


def blogger_bio(request, blogger_id):
    bloger = Blogger.objects.get(id=blogger_id)
    blog_lst = bloger.blogs_set.order_by('-date_post')
    return render(request, 'blogger_bio.html', {'blogger_bio': bloger, 'blog_lst': blog_lst})


def add_comment(request):
    blogs = Blogs.objects.all()
    return render(request, 'add_comment.html', {'blogs': blogs})


def new_post(request):
    return render(request, 'create_post.html')


def krijo_coment(request):
    if request.method == 'POST':
        date_postc = request.POST['date_post']
        permbajtje_c = request.POST['add_comment']
        title_id = request.POST['selected']
        komentuesi_f = request.POST['username']
        t_id = Blogs.objects.only('id').get(title=title_id).id
        id_t = Blogs.objects.get(id=t_id)
        id1 = CommenterUser.objects.only('id').get(username=komentuesi_f).id
        id2 = CommenterUser.objects.get(id=id1)

        coment = Comment.objects.create(date_postc=date_postc, permbajtje_c=permbajtje_c, title_c=id_t,
                                        komentuesi=id2)
        coment.save()
        return redirect('new')
    else:
        return render(request, 'add_comment.html')


def create_new_blog(request):
    return render(request, 'create_post.html')


def add_post(request):
    if request.method == 'POST':
        title = request.POST['add_title']
        date_post = request.POST['date_post']
        author_id = request.POST['your_id']
        permbajtja = request.POST['content']
        id_author = int(author_id)
        id_a = Blogger.objects.get(id=id_author)
        new_post = Blogs.objects.create(title=title, date_post=date_post, author=id_a, permbajtja=permbajtja)
        new_post.save()
        return redirect('new')
    else:
        return render(request, 'create_post.html')
