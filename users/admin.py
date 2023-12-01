from django.contrib import admin
from .models import UserProfile, UserAdress


class AdressAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'adress_line_1',
        'adress_line_2',
        'city',
        'zip_code',
        'country',
        'telephone',
        'mobile_phone',
    )

admin.site.register(UserProfile)
admin.site.register(UserAdress, AdressAdmin)
