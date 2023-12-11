from django.contrib import admin
from .models import Order, OrderItem

class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('orderitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = (
        'order_number',
        'order_date',
        'shipping_cost',
        'order_total',
        'grand_total',
    )

    fields = (
        'order_number',
        'order_date',
        'full_name',
        'email',
        'phone',
        'country',
        'zip_code',
        'city',
        'adress_line_1',
        'adress_line_2',
        'shipping_cost',
        'order_total',
        'grand_total',
    )

    list_display = (
        'order_number',
        'order_date',
        'full_name',
        'shipping_cost',
        'order_total',
        'grand_total',
    )

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)