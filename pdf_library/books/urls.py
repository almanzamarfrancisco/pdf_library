from django.urls import path
from .views import search_books, download_book, list_books

urlpatterns = [
    path('', search_books, name='search_books'),
    path('download/<int:book_id>/', download_book, name='download_book'),
    path('list/', list_books, name='list_books'),
]
