from django.core.management.base import BaseCommand
from website.models import Client, Orders, Items
from faker import Faker
from django.utils import timezone
from random import randint
from datetime import timedelta

faker = Faker()

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)

    def handle(self, *args, **options):
        pk = options.get('pk')
        client = Client.objects.filter(pk=pk).first()
        for i in range(5):
            pk_items = randint(1, 12)
            items = Items.objects.filter(pk=pk_items).first()
            order = Orders(client=client)
            order.save()
            order.item.add(items)
            order.date_time_reg = self.get_date()
            order.save()

    def get_date(self):
        start_date = timezone.now() - timedelta(days=365)
        end_date = timezone.now()
        return faker.date_time_between(start_date=start_date, end_date=end_date).replace(tzinfo=timezone.get_current_timezone())