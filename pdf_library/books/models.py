from django.db import models
from itertools import chain

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pdf = models.CharField(max_length=255)
    book_id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=255)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publisher = models.CharField(max_length=255)
    isbn = models.BigIntegerField() 
    page_count = models.IntegerField()
    language = models.CharField(max_length=255)
    class Meta:
        abstract = True

class BookDefault(Book):
    class Meta:
        db_table = 'books'
        managed = False
        app_label = 'default'

class BookSecond(Book):
    class Meta:
        db_table = 'books'
        managed = False
        app_label = 'second'

class UnifiedBookManager(models.Manager):
    def get_queryset(self):
        from .models import BookDefault, BookSecond
        qs1 = BookDefault.objects.all()
        qs2 = BookSecond.objects.all()
        return list(chain(qs1, qs2))

class UnifiedBook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pdf = models.CharField(max_length=255)
    book_id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=255)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publisher = models.CharField(max_length=255)
    isbn = models.BigIntegerField() 
    page_count = models.IntegerField()
    language = models.CharField(max_length=255)
    objects = UnifiedBookManager()

    class Meta:
        managed = False
        db_table = 'unified_books'
