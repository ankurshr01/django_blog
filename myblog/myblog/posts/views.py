from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def home(request):

	posts=Post.objects.order_by('-date')
	return render(request,'posts/home.html', {'posts':posts})

def post_details(request,post_id):
	post=get_object_or_404(Post,pk=post_id)
	return render(request, 'posts/posts_detail.html', {'post':post})


def contact(request):
	return render(request,'posts/contact.html')

def home1(request):
    return render(request,'posts/home1.html')

def about(request):
    return render(request,'posts/about.html')    	