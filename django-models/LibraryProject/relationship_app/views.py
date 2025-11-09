from django.shortcuts import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    
    output = ""
    for book in books:
        output += f"{book.title} by {book.author.name}\n"

    if not output:
        output = "No books available."
    
    return HttpResponse(output, content_type="text/plain")

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'