from django.shortcuts import render, redirect, HttpResponse
from MyBlog_blog.models import Blog
from MyBlog_blog.forms import ContactForm

from django.contrib.auth.decorators import login_required


def IndexView(request):
    blog = Blog.objects.order_by('-created_date')
    context = {
        "blog": blog
    }
    return render(request, 'web/index.html', context)

def AboutView(request):
    return render(request, 'web/about.html')

def BlogDetailView(request,id):
    blog = Blog.objects.get(id=id)
    context = {
        "blog": blog
    }
    return render(request, 'web/blog-detail.html',context)

def ContactView(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        Contact = form.save(commit=True)
        return redirect("MyBlog_blog:contact")
    context = {
        "form": form
    }
    return render(request, 'web/contact.html',context)

@login_required
def ExampleLoginRequiredView(request):
    return render(request, 'web/index.html')