from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment, Category, Tag
from account.models import User
from mainapp.forms import PostForm, CommentForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def main(request):
    post = Post.objects.all()
    category = Category.objects.all()
    tag = Tag.objects.all()
    count = Post.objects.count()
    return render(request, 'main.html',{'post':post,'category':category, 'tag':tag, 'count':count })


def board_post(request):
    if request.method == 'POST' or request.method=='FILES': #POST요청 폼의 버튼을 눌렀다
        form  = PostForm(request.POST, request.FILES) #form 유효성 확인
        if form.is_valid():
            c = form.save(commit=False) #db에 당장 저장x
            c.user = request.user
            c.save()
            c.Tag.add(*c.extract_tag_list())  # 태그 추가
            messages.success(request, '포스팅을 저장했습니다.')
            return redirect('board_detail', pk = c.pk)
    else: #GET요청 웹 브라우저에서 페이지 접속
        form = PostForm()
    return render(request, 'board_post.html', {'form':form})

def board_detail(request, pk):
    # all = comm.objects.all()
    p = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    # reform = ReCommentForm()
    return render(request, 'board_detail.html', {'post':p, 'form':form})

# 댓글 생성
def comment_create(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) #db에 당장 저장x
            comment.post = post
            comment.user = request.user
            comment.save()
        return redirect('board_detail', pk)

# 댓글 수정
def comment_update(request, pk):
    c = get_object_or_404(Comment,pk=pk) 
    p = get_object_or_404(Post,pk=c.post.pk)
    if(request.method == "POST"):
        form = CommentForm(request.POST, instance=c)
        if(form.is_valid()):
            c = form.save(commit=False)
            c.save()
        return redirect('board_detail', pk=p.pk)
    else:
        form = CommentForm(instance=c) 
        return render(request, 'comment_post.html', {'form':form})

# 댓글 삭제
def comment_delete(request, pk):
    c = get_object_or_404(Comment,pk=pk)
    p = get_object_or_404(Post, pk=c.post.pk)
    c.delete()
    return redirect('board_detail', pk=p.pk)

def scrap(request, pk):
    post = get_object_or_404(Post, pk=pk) # pk값에 해당하는 게시물 받아옴
    user = request.user
    if user in post.scrap.all(): # 요청 유저가 이미 스크랩을 했으면
        post.scrap.remove(user) # 유저 삭제
    else: # 스크랩을 아직 안한 유저라면
        post.scrap.add(user) # 스크랩 목록에 요청 유저 추가
    return redirect('board_detail', pk)

def scrap_list(request):
    user = request.user
    return render(request, 'mypage.html', {'user':user})
    
def category_page(request, name):
    category = Category.objects.get(name=name)

    return render(
        request,
        'category_page.html',
        {
            'post_list': Post.objects.filter(category=category),
            'categories': Category.objects.all(),
            'category': category
        }
    )

def tag_page(request,name):
    tag = Tag.objects.get(name=name)

    return render(
        request,
        'tag_page.html',
        {
            'post_list': Post.objects.filter(Tag=tag),
            'tags': Tag.objects.all(),
            'tag': tag
        }
    )

def search(request):
    if request.method == 'POST':
            search = request.POST['search']        
            post = Post.objects.filter(
                Q(content__contains=search)| 
                Q(category__name__contains=search)| 
                Q(Tag__name__contains=search)| 
                Q(title__contains=search)
            ).distinct()
            # content= Post.objects.filter(content__contains=search)
            # category = Post.objects.filter(category__name__contains=search)
            # tag = Post.objects.filter(Tag__name__contains=search)
            # c = Category.objects.filter(name__contains=search)
            # t = Tag.objects.filter(name__contains = search)
            # return render(request, 'search.html', {'search': search, 'title':title, 'content':content, 'category':category, 'tag':tag})
            return render(request, 'search.html', {'post':post, 'search':search })

    else:
        return render(request, 'search.html', {})


def vote(request):
    post = Post.objects.all()
    return render(request, 'vote.html', {'post':post})

def vote_to(request):
    user = request.user
    if user.vote != None: # 투표내역이 있으면
        messages.error(request, '이미 투표하였습니다.')
    else: 
        selection = request.POST['choice'] # choice라는 이름으로 보낸 POST 요청을 selection이라는 변수에 담음.
        choice = get_object_or_404(Post, id=selection) # id=selection인 (POST 요청을 보낸) Post를 받아옴 
        choice.count += 1 # 해당 게시물의 count +1
        choice.save()
        user.vote = choice # 요청 유저의 vote 내역에 저장
        user.save()
    return redirect('vote')

def vote_result(request):
    post = Post.objects.all().order_by('-count')
    return render(request, 'vote_result.html', {'post':post})

def landing(request):
    post = Post.objects.all()
    category = Category.objects.all()
    tag = Tag.objects.all()
    count = Post.objects.count()
    return render(request, 'landing.html',{'post':post,'category':category, 'tag':tag, 'count':count})

def about(request):
    return render(request, 'about.html')

