from django.shortcuts import render
from django.shortcuts import redirect
from .models import BoardModel

# Create your views here.


def indexfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'index.html', {'object_list':object_list})

def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

def dangerousfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.dangerous = post.dangerous + 1
    post.save()
    return redirect('index')