
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def board_list(request):
    posts = Post.objects.all()
    return render(request, 'cobo/board_list.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cobo:board_list')  # 작성 완료 후 게시물 목록 페이지로 리디렉션
    else:
        form = PostForm()
    return render(request, 'cobo/post_create.html', {'form': form})

def post_detail(request):
    return render(request, 'cobo/post_detail.html')

