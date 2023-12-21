from django.contrib import admin
from .models import CustomShirt

class CustomShirtAdmin(admin.ModelAdmin):
    readonly_fields = ('full_name','email','phone','inquiry','image_tag','created_at',)
    fields = ('image_url','inquiry','image_tag',)
    list_display = (
        'full_name',
        'email',
        'phone',
        'inquiry',
        'image',
        'created_at',
    )

    ordering = ('-created_at',)

admin.site.register(CustomShirt, CustomShirtAdmin)