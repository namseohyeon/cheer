from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Category
from mainapp.forms import PostForm
# Create your views here.
def main(request):
    post = Post.objects.all()
    category = Category.objects.all()
    # count = Category.objects.filter(name=)
    return render(request, 'main.html',{'post':post, 'category':category})


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
    # c = get_object_or_404(Category, pk=pk)
    # form = CommentForm()
    # reform = ReCommentForm()
    return render(request, 'board_detail.html',{'post':p, 'category':p.category.name})

def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    post_list = Post.objects.filter(category=category)
    post = Post.objects.all()
    return render(
        request,
        'category_page.html',
        {
            'post_list':post_list,
            'cotegories':Category.objects.all(),
            'category':category,
            'post':post,
        }
    ) 