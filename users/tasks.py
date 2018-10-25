from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

from celery import shared_task


@shared_task
def bulk_create_users_task(users):
    users = [User(username=user['username'], email=user['email'], password=user['password']) for user in users]
    total = len(users)
    User.objects.bulk_create(users)
    send_mail(
        "Os usuários foram criados com sucesso!",
        f'Foram criados um total de {total} usuarios!',
        settings.DEFAULT_EMAIL,
        ['user@example.com'],
    )
