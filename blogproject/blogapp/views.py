from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Post
from .forms import PostForm

def index(request):
    template = loader.get_template('home.html')
    context = {
        'hava_durumu': "boklu",
    }
    return HttpResponse(template.render(context, request))


def create_post(request):
    error = False
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    context = {
        'form':form,
        'error': False,
    }
    return render(request, 'createpost.html', context)