from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, Http404
from django.template import loader


from .models import Post

# Index Hello Mini test
def index(request):
    latest_post_list = Post.objects.order_by('-published_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'ursitey/index.html', context)


# Detail 404 Error
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'ursitey/detail.html', {'post': post})


# Result
def results(request, post_id):
    response = 'Result for post %s.'
    return HttpResponse(response % post_id)


# Voted
def vote(request, post_id):
    return HttpResponse('You\'ve voted for post %s.' % post_id)
