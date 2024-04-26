from faker import Faker
from django.core.management.base import BaseCommand, CommandParser
from website.models import Items 
from random import randint
faker = Faker()


class Command(BaseCommand):


    def handle(self, *args, **kwargs) -> None:
        acc = {

            'twitter': 10,
            'facebook': 16,
            'instagram': 50,
            'youtube': 100,
            'tiktok': 67,
            'vk': 1,
            'whatsapp': 70,
            'telegram': 150,
            'viber': 14,
            'linkedin': 500,
            'pinterest': 1.5,

        }
        for key, values in acc.items():
            item = Items(name=key, description=f'Description of the item {key}', price=values, quantity=randint(100, 1000))
            item.save()