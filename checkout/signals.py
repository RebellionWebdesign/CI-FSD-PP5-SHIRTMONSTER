from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """ Updates the order_total value on item update/create """
    print("ON SAVE WORKS!")
    instance.order.update_total()


@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    """ Updates the order_total value on item delete """
    print("ON DELETE WORKS!")
    instance.order.update_total()