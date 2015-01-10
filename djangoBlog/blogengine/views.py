#from django.template import RequestContext, loader
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from blogengine.models import Post

class IndexView(generic.ListView):
	template_name = 'blogengine/index.html'
	context_object_name = 'post_list'
	
	def get_queryset(self):
		return Post.objects.all()

class DetailView(generic.DetailView):
	template_name = 'blogengine/detail.html'
	model = Post
