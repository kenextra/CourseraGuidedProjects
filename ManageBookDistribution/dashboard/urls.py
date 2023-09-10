from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('about/', views.about, name='dashboard-about'),
    path('table/', views.table, name='dashboard-table'),
    path('report/', views.report, name='dashboard-report'),
]
