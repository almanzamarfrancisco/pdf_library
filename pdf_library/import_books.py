import csv
import os
from django.conf import settings
from books.models import BookDefault

def import_books(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book = BookDefault(
                title=row['title'],
                author=row['author'],
                pdf=os.path.join('books/pdfs/', row['pdf'])
            )
            book.save()

if __name__ == "__main__":
    import_books('MOCK_DATA.csv')
