from django.shortcuts import render

def index(request):
    reversed_posts = list(reversed(posts))
    return render(request, 'blog/index.html', {'posts': reversed_posts})


def post_detail(request, id):
    post = next((p for p in posts if p['id'] == id), None)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    filtered_posts = [
        post for post in posts if post['category'] == category_slug]
    return render(request, 'blog/category.html', {
        'category_slug': category_slug,
        'posts': filtered_posts,
    })
