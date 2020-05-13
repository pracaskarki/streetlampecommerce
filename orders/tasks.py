from celery import task
from django.core.mail import send_mail
from .models import Order
from io import BytesIO
from celery import task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f' Your Order id is {order.id}.'
    mail_sent = send_mail(subject, message, 'prakashkarkifive1@gmail.com',[order.email], fail_silently=False )
    return mail_sent
