import os
from django.conf import settings
from email.mime.image import MIMEImage
from datetime import date

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_thanks_email(first_name, last_name, email, donation):
    strFrom = settings.EMAIL_FROM
    ctx = {
        'first_name': first_name,
        'last_name': last_name,
        'email_address': email,
        'donation': str(donation),
        'date': date.today()}

    html_content = render_to_string('mail.html', context=ctx).strip()

    subject = 'Thank you for your donation to Funsepa!'
    recipients = [email]
    reply_to = [settings.EMAIL_REPLY_TO]

    msg = EmailMultiAlternatives(subject, html_content, strFrom, recipients, reply_to=reply_to)
    msg.content_subtype = 'html'
    msg.mixed_subtype = 'related'

    image_list = [
        'logo.jpg',
        'foto.jpg',
        'fb.png',
        'ig.png',
        'link.png',
        'tw.png',
        'yt.png',
        'snap.png']

    for img in image_list:
        fp = open(os.path.join(settings.BASE_DIR, 'pagos/static/img/email/' + img), 'rb')
        image = MIMEImage(fp.read())
        image.add_header('Content-ID', '<{}>'.format(os.path.basename(fp.name)))
        msg.attach(image)
        fp.close()

    msg.send()
