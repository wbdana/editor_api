from django.contrib import admin
from .models import Owner, Collaborator, Reader, Record

# Register your models here.
admin.site.register(Owner)
admin.site.register(Collaborator)
admin.site.register(Reader)
admin.site.register(Record)
