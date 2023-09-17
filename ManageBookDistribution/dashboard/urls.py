from django.urls import path
from dashboard.views import (
    BookListView, BookDetailView,
    BookCreateView, BookUpdateView,
    BookDeleteView, UserBookListView,
    CategoryListView, BookCategoryListView,
    AuthorBookListView
)
from dashboard import views

urlpatterns = [
    path('', BookListView.as_view(), name='dashboard-home'),
    path('user/<str:username>', UserBookListView.as_view(), name='user-books'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('about/', views.about, name='dashboard-about'),
    path('category/', CategoryListView.as_view(), name='dashboard-category'),
    path('category/<int:pk>/', BookCategoryListView.as_view(),
         name='category-detail'),
    path('author/<str:authors>/', AuthorBookListView.as_view(),
         name='author-books'),
    path('report/', views.report, name='dashboard-report'),
]
