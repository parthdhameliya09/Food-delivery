from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import uuid
from django.conf import settings
from django.core.mail import send_mail

def send_forgot_password_mail(email, token):
    subject = 'Your Forgot Password Link'
    message = f'Hii, click on the link to reset your password http://127.0.0.1:8000/changepwd/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recepient_list = [email]
    send_mail(subject, message, email_from, recepient_list)
    return True