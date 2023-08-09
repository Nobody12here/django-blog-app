from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from .form import EmailForm
# Create your views here.
class PostListView(ListView):
	 #Fetches the post irrespective of the status
	queryset = Post.published.all()
	context_object_name = 'posts'
	paginate_by = 3
	template_name = 'blog/post/list.html'

def post_details(request,year,month,day,post):
	try:
		post = get_object_or_404(Post,status=Post.Status.PUBLISHED,slug=post,
			publish__year=year,publish__month=month,publish__day=day
		) #Fetches the post with the given slug and publish date
	except Post.DoesNotExist:
		raise Http404('Post does not exists')
	
	return render(request,'blog/post/details.html',{'post':post})
def post_share(request,post_id):
	post = get_object_or_404(Post,id=post_id,status=Post.Status.PUBLISHED)
	sent = False
	if(request.method == 'POST'):
		form = EmailForm(request.POST)
		print("Email_Form = ",form)
		if (form.is_valid()):
			cd = form.cleaned_data
			post_url = request.build_absolute_uri(
				post.get_absolute_url() )
			subject = f"{cd['name']} recommmends you read {post.title}"
			message = f"Read {post.title} at {post_url}\n\n {cd['name']}\'s commentst {cd['comments']}"
			send_mail(subject,message,'uraja01212@gmail.com',[cd['to']])
			sent= True
	else:
		form = EmailForm()
	return render(request,'blog/post/share.html',{'post':post,'form':form})