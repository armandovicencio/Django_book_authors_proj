from django.urls import path
from . import views



urlpatterns = [
    path('add_book', views.add_book, name="add_book"),
    path('book_detail/<int:book_id>', views.book_detail, name="book_detail"),
    path('', views.all_books, name="books"),

    path('add_author', views.add_author, name="add_author"),
    path('authors/<int:author_id>', views.author_detail, name="author_detail"),
    path('authors', views.all_authors, name="authors"),
    path('add_book_to_author', views.add_book_to_author, name="add_book_to_author")
]
