from django.urls import path
from . import views

app_name = "algo_explained"
urlpatterns = [
        path("all_posts/", views.blog_index, name="blog_index"),
        path("<int:pk>/", views.blog_detail, name="blog_detail"),
        path("<category>/", views.blog_category, name="blog_category"),

]
