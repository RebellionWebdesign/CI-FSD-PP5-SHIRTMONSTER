from django.contrib import admin
from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'phone',
        'country',
        'zip_code',
        'city',
        'adress_line_1',
        'adress_line_2',
    )


admin.site.register(UserProfile)
