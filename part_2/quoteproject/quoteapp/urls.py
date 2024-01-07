# quoteapp/urls.py


from django.urls import path
from quoteproject.quoteapp import views

app_name = 'quoteapp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('author-list/', views.author_list, name='author_list'),
    path('quote-list/', views.quote_list, name='quote_list'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-quote/', views.add_quote, name='add_quote'),
]

