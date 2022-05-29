from django.urls import path

from django_education import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('home_page/', views.home, name="home_page"),
    path('delete_last_post/', views.delete_last_post, name="delete_last_post"),
    path("post/<int:id>", views.post_detailes, name="post_id")
]
