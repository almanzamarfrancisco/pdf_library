from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
from .models import UnifiedBook, BookDefault, BookSecond
from .forms import BookSearchForm
from django.conf import settings
import os
def search_books(request):
    form = BookSearchForm()
    books = []
    if request.method == 'GET':
        form = BookSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = get_book_from_dbs_by_title(query)
    return render(request, 'books/search.html', {'form': form, 'books': books})

def download_book(request, book_id):
    book = get_book_from_dbs(book_id)
    if not book:
        raise Http404("Book not found.")
    find_pdf = ''
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, book.pdf)
    if not os.path.isfile(file_path):
        raise Http404("PDF file not found.")
    response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(book.title)}"'
    return response

def list_books(request):
    books = UnifiedBook.objects.all()
    return render(request, 'books/list_books.html', {'books': books})

def get_book_from_dbs(book_id):
    try:
        return BookDefault.objects.get(book_id=book_id)
    except BookDefault.DoesNotExist:
        try:
            return BookSecond.objects.get(book_id=book_id)
        except BookSecond.DoesNotExist:
            return None
def get_book_from_dbs_by_title(title):
    try:
        return BookDefault.objects.filter(title__icontains=title)
    except BookDefault.DoesNotExist:
        try:
            return BookSecond.objects.filter(title__icontains=title)
        except BookSecond.DoesNotExist:
            return None
