from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status=Post.Status.PUBLISHED)

# Create your models here.
class Post(models.Model):
	#Create a custom manager
	objects = models.Manager()
	published = PublishedManager()
	#Basic Fields that every post should have
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250,unique_for_date='publish')
	body = models.TextField()
	#Date and time the post was created,updated,published
	created = models.DateTimeField(auto_now_add=True)
	publish = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(auto_now=True)
	#Author of the post
	author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
	#Add a status field to indicate whether the post is published or not
	class Status(models.TextChoices):
		DRAFT = 'DF','draft'
		PUBLISHED = 'PB','published'
	status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
	# add the default order to retrieve the posts
	class Meta:
		ordering = ['-publish']
		indexes = [
			models.Index(fields=['-publish'])
		]

	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('blog:post_detail',args=
			[self.publish.year,
			self.publish.month,
			self.publish.day,
			self.slug])


