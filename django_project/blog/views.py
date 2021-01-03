from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# posts = [
#     {
#         'author': 'Prakhar',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'December 31 2020',
#         'contact': '8874109902'
#     },
#     {
#         'author': 'Yush',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'December 30 2020',  
#         'contact': '6386373789'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,  'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def contact(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/contact.html', context)


