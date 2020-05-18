from django.shortcuts import render

# Create your views here.
from .models import Post

def index(request):
	posts = Post.objects.all();
	categories = Post.objects.values('category').distinct();
	contex = {
		'title':'Home Blog',
		'subTitle' : 'Blog',
		'content':'ini adalah halaman blog',
		'Categories':categories,
		'Posts':posts,
	}

	return render(request,'blog/index.html',contex)

def categoryPost(request,categoryInput):
	posts = Post.objects.filter(category=categoryInput);
	categories = Post.objects.values('category').distinct();
	contex = {
		'title':'Home Blog',
		'subTitle' : 'Blog',
		'content':'tampilkan berdasarkan category',
		'Categories':categories,
		'Posts':posts,
	}

	return render(request,'blog/category.html',contex)


def detailPost(request,slugInput):
	posts = Post.objects.get(slug=slugInput);
	categories = Post.objects.values('category').distinct();
	contex = {
		'title':'Home Blog',
		'subTitle' : 'Blog',
		'content':'ini adalah halaman blog',
		'Categories':categories,
		'Posts':posts,
	}

	return render(request,'blog/detail.html',contex)