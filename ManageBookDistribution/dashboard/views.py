from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from .models import Book


# Create your views here.
def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'dashboard/home.html', context)

def table(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'dashboard/tables.html', context)

# view the distribution expenses of books according to their categories
# https://hackmamba.io/blog/2022/03/quickly-create-interactive-charts-in-django/
def report(request):
    books = Book.objects.all()
    data = [ 
            {'category': x.category,
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

def about(request):
    return render(request, 'dashboard/about.html', {'title': 'About'})
