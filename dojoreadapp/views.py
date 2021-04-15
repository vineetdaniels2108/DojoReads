from django.shortcuts import render, redirect, HttpResponse
from .models import *
from loginapp.models import User 
from django.contrib import messages

# Create your views here.

def dojoindex(request):
    logged_user = User.objects.get(id = request.session['user'])
    top_3_reviews = Reviews.objects.order_by('-updated_at')[:3]
    all_reviews = Reviews.objects.all()
    books = []
    for review in all_reviews:
        if review.book not in books:
            books.append(review.book)
    context = {
        'user': logged_user,
        'top_3': top_3_reviews,
        'all_reviews' : all_reviews,
        'books': books
    }
    return render (request, 'dojoread.html',context)

def home(request):
    return redirect ('/dojoread')

def add_book_page(request):
    logged_user = User.objects.get(id = request.session['user'])
    all_books = Books.objects.all()
    author = []
    for book in all_books: 
        if book.author not in author:
            author.append(book.author)
    context = {
        'user': logged_user,
        'books': all_books,
        'authors': author
    }
    return render (request, 'add_book.html', context)

def add_book(request):
    author_1 = request.POST['existing_author']
    author_2 = request.POST['new_author']
    if request.method == 'POST':
        logged_user = User.objects.get(id = request.session['user'])
        title = request.POST['title']
        if len(author_2)==0:
            new_author = author_1
        else:
            new_author = author_2
        review = request.POST['review']
        rating = request.POST['rating']
        new_book = Books.objects.create(title = title, author = new_author, rating = rating, uploaded_by= logged_user)
        new_review = Reviews.objects.create(review = review, posted_by= logged_user, book = new_book)
        book_id = new_book.id
        
        return redirect (f'/dojoread/{book_id}/show_book')
    else:
        return redirect ('/dojoread/add')
    
def show_book(request, book_id):
    logged_user = User.objects.get(id = request.session['user'])
    book = Books.objects.get(id = book_id)
    book_reviews = book.book_reviews.all()
    users_reviews = []
    for review in book_reviews:
        users_reviews.append(review.posted_by)
    context = {
        'user': logged_user,
        'book': book,
        'reviews': book_reviews,
        'user_reviews': users_reviews
    }
    
    return render(request, 'show_book.html', context)

def add_review(request, book_id):
    logged_user = User.objects.get(id = request.session['user'])
    book = Books.objects.get(id = book_id)
    if request.method == 'POST':
        review = request.POST['review']
        new_review = Reviews.objects.create(review = review, posted_by= logged_user, book = book)
        return redirect (f'/dojoread/{book_id}/show_book')
    else:
        return redirect (f'/dojoread/{book_id}/show_book')
    
def delete_review(request, review_id, book_id):
    review = Reviews.objects.get(id=review_id)
    review.delete()
    return redirect (f'/dojoread/{book_id}/show_book')

def show_user(request, user_id):
    logged_user = User.objects.get(id = request.session['user'])
    user_info = User.objects.get(id = user_id)
    user_reviews = user_info.user_post.all()
    review_count = len(user_reviews)
    context = {
        'user' : logged_user,
        'user_info': user_info,
        'count': review_count,
        'user_reviews': user_reviews
    }
    
    return render (request, 'show_user.html', context)