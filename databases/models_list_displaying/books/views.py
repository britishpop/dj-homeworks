from django.views import generic
from django.shortcuts import get_object_or_404
from books.models import Book
from datetime import datetime


class BookListView(generic.ListView):
    model = Book
    # template_name = 'books/book_by_date.html'
    context_object_name = 'books'
    

class BookDateView(generic.ListView):
    model = Book
    template_name = 'books/book_by_date.html'
    context_object_name = 'books'

    def get_queryset(self):
        self.name = get_object_or_404(Book, pub_date=self.kwargs['pub_date'])
        return Book.objects.filter(name=self.name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        published_date = context['books'][0].pub_date
        
        try:
            nextdate = Book.objects.filter(
                    pub_date__gt=published_date
                ).order_by(
                    'pub_date'
                ).first().pub_date
        except AttributeError:
            nextdate = published_date
        
        try:
            prevdate = Book.objects.filter(
                    pub_date__lt=published_date
                ).order_by(
                    '-pub_date'
                ).first().pub_date
        except AttributeError:
            prevdate = published_date

        context['next'] = datetime.strftime(nextdate, "%Y-%m-%d")
        context['previous'] = datetime.strftime(prevdate, "%Y-%m-%d")

        return context
