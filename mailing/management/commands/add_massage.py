from django.core.management import BaseCommand

from mailing.models import Message


class Command(BaseCommand):

    def handle(self, *args, **options):
        Message.objects.all().delete()

        message_list = [
            {'header': 'Приветствие',
             'body': 'Добрый день!',
             },
            {'header': 'Акции',
             'body': 'Наши новые Акции!',
             },
            {'header': 'Программа лояльности',
             'body': 'Праила программы лояльности!',
             },
        ]

        message_objects = []

        for item in message_list:
            message_objects.append(Message(**item))
        Message.objects.bulk_create(message_objects)
