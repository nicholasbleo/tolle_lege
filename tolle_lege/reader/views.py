from django.shortcuts import render, get_object_or_404
from .models import Book, Page, Morpheme
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

@login_required
def library(request):
    books = Book.objects.all()
    return render(request,
                  'reader/books/library.html',
                  {'books': books})

@login_required
def book_pages(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    pages = book.pages.all()
    return render(request,
                  'reader/books/book-pages.html',
                  {'pages': pages, 'book': book})

@login_required
def book_page(request, book_id, page_id):
    page = get_object_or_404(Page, book=book_id, id=page_id)
    words = page.words.all()
    return render(request,
                  'reader/books/page.html',
                  {'page': page, 'words': words})

@login_required
@require_POST
def parse_morpheme(request):
    morpheme_id = request.POST.get('id')
    action = request.POST.get('action')
    if morpheme_id and action:
        try:
            morpheme = Morpheme.objects.get(id=morpheme_id)
            if action == 'parse':
                print('Parse')
            else:
                print("Can't parse")
            return JsonResponse({'status': 'ok'})
        except Morpheme.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})