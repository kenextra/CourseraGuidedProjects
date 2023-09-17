from django.contrib.auth.models import User
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from dashboard.models import Book, Category


class BookResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category',
                            widget=ManyToManyWidget(model=Category,
                                                    field='name',
                                                    separator=None,),)
    added_by = fields.Field(attribute='added_by',
                            widget=ForeignKeyWidget(model=User,
                                                    field='username'))
    
    def __init__(self, user):
        self.user = user
          
    def before_save_instance(self, instance, using_transactions, dry_run):
        instance.added_by = self.user
    
    
    class Meta:
        model = Book
