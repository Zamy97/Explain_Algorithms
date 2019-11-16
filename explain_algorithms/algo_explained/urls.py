from django.urls import path
from explain_algorithms.algo_explained.views import (
    blog_index,
    blog_detail,
    blog_category,
)

app_name = "algo_explained"
urlpatterns = [
        path("all_posts/", view = blog_index, name="blog_index"),
        path("<int:pk>/", view = blog_detail, name="blog_detail"),
        path("<category>/", view = blog_category, name="blog_category"),

]
