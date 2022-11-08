from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from mainapp.forms import PostForm
# Create your views here.
def main(request):
    post = Post.objects.all()
    return render(request, 'main.html',{'post':post})


def board_post(request):
    if request.method == 'POST' or request.method=='FILES': #POST요청 폼의 버튼을 눌렀다
        form  = PostForm(request.POST, request.FILES) #form 유효성 확인
        if form.is_valid():
            c = form.save(commit=False) #db에 당장 저장x
            c.user = request.user
            c.save()
            return redirect('board_detail', pk = c.pk)
    else: #GET요청 웹 브라우저에서 페이지 접속
        form = PostForm()
    return render(request, 'board_post.html', {'form':form})

def board_detail(request, pk):
    # all = comm.objects.all()
    p = get_object_or_404(Post, pk=pk)
    # form = CommentForm()
    # reform = ReCommentForm()
    return render(request, 'board_detail.html',{'post':p})