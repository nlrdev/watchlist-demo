from django.contrib import admin
from .models import CryptoPair

@admin.register(CryptoPair)
class CryptoPairAdmin(admin.ModelAdmin):
    pass