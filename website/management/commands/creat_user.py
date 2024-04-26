from django.core.management.base import BaseCommand
from website.models import Client
from faker import Faker
from random import randint


faker = Faker()

class Command(BaseCommand):


    def add_arguments(self, parser) -> None:
        parser.add_argument('count', type=int)

    def handle(self, *args, **options) -> None:
        count = options.get('count')
        rand = randint(0, 10)
        for _ in range(count - 1):
            client = Client(name=faker.name(), email=faker.email(), phone=f'89{rand}120{rand}554{rand}', address=faker.address())
            client.save()
