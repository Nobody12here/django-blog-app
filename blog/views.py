from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def post_list(request):
	 #Fetches the post irrespective of the status
	posts_lists = Post.published.all()
	# 3 Posts per page
	paginator = Paginator(posts_lists,3)
	page_number = request.GET.get('page',1)
	try:
		posts = paginator.page(page_number)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	except PageNotAnInteger:
		posts = paginator.page(1)


	

	return render(request,'blog/post/list.html',{'posts':posts})

def post_details(request,year,month,day,post):
	try:
		post = get_object_or_404(Post,status=Post.Status.PUBLISHED,slug=post,
			publish__year=year,publish__month=month,publish__day=day
		) #Fetches the post with the given slug and publish date
	except Post.DoesNotExist:
		raise Http404('Post does not exists')
	
	return render(request,'blog/post/details.html',{'post':post})