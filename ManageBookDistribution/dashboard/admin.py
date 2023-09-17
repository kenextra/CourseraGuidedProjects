from django.contrib import admin
from .models import Book, Category
from dashboard.resources import BookResource

# Register your models here.
from import_export.admin import ImportExportModelAdmin

class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [BookResource]
    
    def get_import_resource_kwargs(self, request, *args, **kwargs):
        kwargs = super().get_resource_kwargs(request, *args, **kwargs)
        kwargs.update({"user": request.user})
        return kwargs
    
admin.site.register(Category)
admin.site.register(Book, BookAdmin)