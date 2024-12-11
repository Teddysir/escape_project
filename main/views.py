from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post


def door1_view(request):
    return render(request, 'main/door1.html')

def door2_view(request):
    return render(request, 'main/door2.html')

def door3_view(request):
    return render(request, 'main/door3.html')


def index(request):
    return render(request, 'main/index.html')

def mouse(request):
    return render(request, 'main/mouse.html')

def main(request):
    return render(request, 'main/main.html')



def activate(request):
    posts = Post.objects.all().order_by('-created_at') 
    return render(request, 'main/activate.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'main/detail.html', {'post': post})



def door1(request):
    return render(request, 'main/door1.html') 

def door2(request):
    return render(request, 'main/door2.html') 

def door3(request):
    return render(request, 'main/door3.html') 


def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        image = request.FILES.get('image')

        # 필수 필드 확인
        if not title or not content or not author:
            return HttpResponse('필수 항목이 누락되었습니다.', status=400)

        # 새 게시물 생성
        Post.objects.create(
            title=title,
            content=content,
            author=author,
            image=image
        )

        return redirect('activate')  

    return render(request, 'main/create.html')  


