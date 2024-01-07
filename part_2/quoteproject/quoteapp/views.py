# quoteapp/views.py

import os
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from quoteproject.quoteapp.models import Author, Quote
from quoteproject.quoteapp.forms import AuthorForm, QuoteForm
from django.conf import settings


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Change 'home' to the appropriate URL name for your home page
    else:
        form = UserCreationForm()

    template_path = os.path.join(settings.BASE_DIR, 'author_quote', 'templates', 'registration', 'register.html')

    return render(request, template_path, {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Change 'home' to the appropriate URL name for your home page
    else:
        form = AuthenticationForm()

    template_path = os.path.join(settings.BASE_DIR, 'author_quote', 'templates', 'registration', 'login.html')

    return render(request, template_path, {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')  # Change 'home' to the appropriate URL name for your home page


def author_list(request):
    authors = Author.objects.all()

    template_path = os.path.join(settings.BASE_DIR, 'author_quote', 'templates', 'author_quote', 'author_list.html')

    return render(request, template_path, {'authors': authors})


def quote_list(request):
    quotes = Quote.objects.all()

    template_path = os.path.join(settings.BASE_DIR, 'author_quote', 'templates', 'author_quote', 'quote_list.html')

    return render(request, template_path, {'quotes': quotes})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()

    template_path = os.path.join(settings.BASE_DIR, 'author_quote', 'templates', 'author_quote', 'add_author.html')

    return render(request, template_path, {'form': form})


def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quote_list')
    else:
        form = QuoteForm()

    template_path = os.path.join(settings.BASE_DIR, 'author_quote', 'templates', 'author_quote', 'add_quote.html')

    return render(request, template_path, {'form': form})
