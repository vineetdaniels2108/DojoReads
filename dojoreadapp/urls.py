from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.dojoindex),
    path('/add', views.add_book_page),
    path('/home', views.home),
    path('/add_book', views.add_book),
    path('/<int:book_id>/show_book', views.show_book),
    path('/<int:book_id>/add_review', views.add_review),
    path('/<int:review_id>/<int:book_id>/delete_review', views.delete_review),
    path('/<int:user_id>/show_user', views.show_user)
]