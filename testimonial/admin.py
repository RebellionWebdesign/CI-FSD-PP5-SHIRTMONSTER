from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    readonly_fields = [
        'created_at',
        'modified_at',
    ]
    fields = (
        'user_id',
        'order_id',
        'content',
        'created_at',
        'modified_at',
    )
    list_display = (
        'user_id',
        'order_id',
        'created_at',
        'modified_at',
    )

    ordering = ('-created_at',)


admin.site.register(Testimonial, TestimonialAdmin)
