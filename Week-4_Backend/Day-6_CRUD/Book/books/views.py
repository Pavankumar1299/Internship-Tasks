from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book


def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        price = request.POST.get("price")

        if not title or not author or not price:
            messages.error(request, "All fields are required")
            return redirect("home")

        Book.objects.create(
            title=title,
            author=author,
            price=price
        )

        messages.success(request, "Book added successfully")
        return redirect("home")

    books = Book.objects.all()
    return render(request, "home.html", {"books": books})

def view_books(request):
    books = Book.objects.all()
    return render(request, "home.html", {"books": books})
    
def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.price = request.POST.get("price")
        book.save()

        messages.success(request, "Book updated successfully")
        return redirect("home")

    return render(request, "update.html", {"book": book})
        
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    messages.success(request, "Book deleted")
    return redirect("home")