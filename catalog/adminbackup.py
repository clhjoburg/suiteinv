from django.contrib import admin

# Register your models here.
from .models import sound, live, stem

admin.site.register(sound)
admin.site.register(live)

class StemAdmin(admin.ModelAdmin):
    list_display = '__all__'
    fields = '__all__'

admin.site.register(stem)