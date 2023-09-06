from django.shortcuts import render
from  .models import Post 
# Create your views here.
def index(request):
    obj= Post.objects.all()
    context={
        "obj":obj
    }
    return render(request,"index.html",context)
