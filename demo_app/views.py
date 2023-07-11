from django.shortcuts import render
from .models import Blog
def index(request):
    blogs = Blog.objects.all()
    return render(request,'demo_app/index.html',{'blogs':blogs})