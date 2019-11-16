from django.shortcuts import render
from .models import Post

#blog_index will display a list of all your posts.

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts" : posts,
    }
    return render(request, "blog_index.html", context)


#blog_detail will display the full post as well as comments and a form to allow users to create new comments.
def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


#blog_category will be similar to blog_index, but the posts viewed will only be of a specific category chosen by the user.
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }
    return render(request, "blog_detail.html", context)
