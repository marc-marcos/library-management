from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path("addbook/", views.addbook, name="addbook"),
    path('read_isbn/<str:isbn>/', views.read_isbn, name='read_isbn'),
    path('book/<int:book_id>/', views.book, name='book'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('get/<int:book_id>/', views.get_book, name='get'),
    path('return/<int:book_id>/', views.return_book, name='return'),
]