from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import Http404
# Create your views here.
def post_list(request):
	 #Fetches the post irrespective of the status
	posts = Post.published.all()
	return render(request,'blog/post/list.html',{'posts':posts})

def post_details(request,id):
	try:
		post = get_object_or_404(Post,id=id) #Fetches the post with id irrespective of the status
	except Post.DoesNotExist:
		raise Http404('Post does not exists')
	
	return render(request,'blog/post/details.html',{'post':post})