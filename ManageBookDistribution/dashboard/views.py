from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from dashboard.models import Book, Category


# view the home page
class BookListView(ListView):
    model = Book
    template_name = 'dashboard/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    ordering = ['-date_added']
    paginate_by = 10


# view the categories
class CategoryListView(ListView):
    model = Category
    template_name = 'dashboard/category.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'categories'
    ordering = ['-date_added']
    paginate_by = 10
    

# view the books added by a user
class UserBookListView(ListView):
    model = Book
    template_name = 'dashboard/user_books.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    paginate_by = 10
    
    # get the books added by a user
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Book.objects.filter(added_by=user).order_by('-date_added')


# view the books in a category
class BookCategoryListView(ListView):
    model = Book
    template_name = 'dashboard/category_detail.html'
    context_object_name = 'books'
    paginate_by = 10
    
    # get the books in a category
    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return Book.objects.filter(category=category).order_by('-date_added')
    
    # get the category and add it to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        context["category"] = category
        return context


class AuthorBookListView(ListView):
    model = Book
    template_name = 'dashboard/author_books.html'
    context_object_name = 'books'
    paginate_by = 10
    
    # get the books in a category
    def get_queryset(self):
        print(self.kwargs.keys())
        authors = self.kwargs.get('authors')
        return Book.objects.filter(authors=authors).order_by('-date_added')
    
    
# view the details of a book
class BookDetailView(DetailView):
    model = Book


# create a new book
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['bookID', 'title', 'subtitle', 'authors',
              'publisher', 'published_date', 'category',
              'distribution_expense', 'image']
    
    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)


# update a book
class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['bookID', 'title', 'subtitle', 'authors',
              'publisher', 'published_date', 'category',
              'distribution_expense', 'image']
    
    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        book = self.get_object()
        if self.request.user == book.added_by:
            return True
        return False
    

# delete a book
class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/'
    def test_func(self):
        book = self.get_object()
        if self.request.user == book.added_by:
            return True
        return False



# view the distribution expenses of books according to their categories
# https://hackmamba.io/blog/2022/03/quickly-create-interactive-charts-in-django/
def report(request):
    books = Book.objects.all()
    data = [ 
            {'category': x.category.all()[0].name.capitalize() if x.category.all().exists() else 'Other',
             'expense': x.distribution_expense,
             } for x in books
            ]
    df = pd.DataFrame(data)
    grouped = df.groupby('category', as_index=False).sum()
    fig = px.pie(grouped, values='expense', names='category', title='Distribution Of Expenses by Category')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    expense_plot = plot(fig, output_type='div')
    context = {'plot_div': expense_plot}
    return render(request, 'dashboard/report.html', context)


# view the about page
def about(request):
    return render(request, 'dashboard/about.html', {'title': 'About'})
