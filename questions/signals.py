from django.dispatch import Signal
from django.core.mail import send_mail
from django.db.models.signals import post_save
from models import Answer
from django.contrib.sites.models import Site
from django.conf import settings

post_save = Signal(providing_args=['instance', 'answer'])


def notify_user(sender, instance, answer, **kwargs):
    message = "New answer added to question {0}\nAnswer: {1}\n".format(instance.title, answer)
    message += "See it: http://{0}/{1}/".format(Site.objects.get_current().domain, instance.pk)
    subject = instance.title
    send_mail(subject, message, settings.SERVER_EMAIL, [instance.owner.email, ], fail_silently=False)

post_save.connect(notify_user, sender=Answer)
