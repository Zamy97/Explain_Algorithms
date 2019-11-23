from django.shortcuts import render
from explain_algorithms.algo_explained.models import Post, Comment
from explain_algorithms.algo_explained.forms import CommentForm

#Do the class based view instead of function based view

#blog_index will display a list of all your posts.

# Class ShowBlogs()

def blog_index(request):
    return render(request, "algo_explained/blog_index.html", {})

# def blog_index(request):
#     posts = Post.objects.all().order_by("-created_on")
#     context = {
#         "posts" : posts,
#     }
#     return render(request, "blog_index.html", context)

#
# #blog_detail will display the full post as well as comments and a form to allow users to create new comments.
# def blog_category(request, category):
#     posts = Post.objects.filter(
#         categories__name__contains=category
#     ).order_by(
#         '-created_on'
#     )
#     context = {
#         "category": category,
#         "posts": posts
#     }
#     return render(request, "blog_category.html", context)
#
#
# #blog_category will be similar to blog_index, but the posts viewed will only be of a specific category chosen by the user.
# def blog_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     comments = Comment.objects.filter(post=post)
#
#     form = CommentForm()
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = Comment(
#                 author=form.cleaned_data["author"],
#                 body=form.cleaned_data["body"],
#                 post=post,
#             )
#             comment.save()
#
#     context = {"post": post, "comments": comments, "form": form}
#     return render(request, "blog_detail.html", context)
