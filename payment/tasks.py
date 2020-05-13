from celery import task
from io import BytesIO
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order

@task
def payment_completed(order_id):
    order = Order.objects.get(id=order_id)

    subject = f'StreetLamp Hardwares and Suppliers --Invoice no. {order.id}'
    message = 'Please, find attached invoice for your recent purchase.'
    email = EmailMessage(subject, message, 'prakashkarkifive1@gmail.com', [order.email])

    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string = html).write_pdf(out, stylesheets=stylesheets)

    email.attach(f'Order_{order_id}.pdf', out.getvalue(), 'application/pdf')
    email.send(fail_silently=False)