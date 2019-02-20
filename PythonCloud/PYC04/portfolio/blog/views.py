from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Blog

def blog_page(request):
	blogs = Blog.objects
	return render(request, 'blog.html', {'blogs':blogs})


def blog_text(request,blog_id):
    blog  = get_object_or_404(Blog, pk=blog_id)
    #blogs = Blog.objects, {'blogs':blogs}
    return render(request, 'blog_text.html', {'blog': blog})
