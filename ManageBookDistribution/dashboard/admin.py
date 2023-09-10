from django.contrib import admin
from .models import Book, Category
from dashboard.resources import BookResource

# Register your models here.
from import_export.admin import ImportExportModelAdmin

class BookAdmin(ImportExportModelAdmin):
    resource_classes = [BookResource]

admin.site.register(Category)
admin.site.register(Book, BookAdmin)