from contact.models import Contact
from django.contrib import admin

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'lastName',
                    'email', 'subject', 'created_at')
    list_filter = ('email', 'subject')


admin.site.register(Contact, ContactAdmin)
