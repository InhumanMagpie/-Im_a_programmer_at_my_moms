from django.urls import path

from django_education import views


urlpatterns = [
    path("", views.home, name="home_page"),
    path("home_page/", views.home, name="home_page"),
    path("post/<int:id>", views.post_details, name="post_id"),
    path("add/", views.add_post, name="add_post"),
    path("delete/<int:id>", views.delete_post, name="delete_post"),
]
