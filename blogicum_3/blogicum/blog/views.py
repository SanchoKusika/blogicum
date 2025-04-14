from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_at = timezone.now()
            post.save()
            return redirect('blog:post_detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})


def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/create.html', {'form': form})


def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:index')
    return render(request, 'blog/create.html', {'form': post})


def add_comment(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/comment.html', {'form': form, 'post': post})


def index(request):
    qs = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': qs})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True)
    qs = Post.objects.filter(
        category=category,
        pub_date__lte=timezone.now(),
        is_published=True
    ).order_by('-pub_date')
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': qs,
    })


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        pk=id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})
