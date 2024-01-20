# main_app/admin.py

from django.contrib import admin
from .models import Property, Transaction, Folder

admin.site.register(Property)
admin.site.register(Transaction)
admin.site.register(Folder)

# Register other models as well
