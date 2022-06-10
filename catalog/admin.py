from django.contrib import admin

# Register your models here.

from .models import sound, emaillist, stem, live, livelarge, contact

admin.site.register(sound)
admin.site.register(live)
admin.site.register(livelarge)

class ContactAdmin(admin.ModelAdmin):
    list_display = '__all__'
    fields = '__all__'

admin.site.register(contact)

class StemAdmin(admin.ModelAdmin):
    list_display = '__all__'
    fields = '__all__'

admin.site.register(stem)


class EmailListAdmin(admin.ModelAdmin):
    list_display = ('email', 'country',)
    fields = ['email', 'country']

admin.site.register(emaillist, EmailListAdmin)

