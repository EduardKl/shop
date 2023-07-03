from celery import shared_task
from django.core.mail import send_mail
from shop_site import settings
from .models import Order


@shared_task
def order_created(order_id):
    """
    Задание по отправке уведобления на электронную почту клиента
    при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    
    mail_sent = send_mail(f'Заказ {order.id} оформлен.',
                      f'Заказ {order.id} оформлен.',
                      settings.EMAIL_HOST_USER,
                      [order.email], 
                      fail_silently=False)

    return mail_sent
