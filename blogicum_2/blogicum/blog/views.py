from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


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
