from django.shortcuts import render
from django.http import HttpResponse
import logging
from .models import Client, Items, Orders
from django.views import View
from django.utils import timezone
from datetime import timedelta
from .forms import ImageDownload
from django.core.files.storage import FileSystemStorage


logger = logging.getLogger(__name__)

def main_page(request):
    logger.info("все отлично)")
    html = """
                Hi, you have come to a store specializing in providing accounts in various, popular at the moment servers, on just a fraction of the inernet.
            """
    return HttpResponse(html)

def about_yourself(request):
    logger.info("все отлично и теперь даже лучше)")
    html = """
                If you came to this page it means you need new accounts, I don't ask you why you need them, then don't ask me about me! Go do what you came to do, do it friend.
            """ 
    return HttpResponse(html)


def creat_client(request):
    for i in range(1, 5):
        Client.creat_client(name=f"name{i}", phone=f"8901207554{i}", email=f"email{i}@gmail.com", address=f"street{i}")
    return HttpResponse("ok")

def creat_items(request):
    for i in range(1, 5):
        Items.creat_item(name=f"name{i}", price=f"{i*4}", description=f"description{i}", quantity="100")
    return HttpResponse("ok")

def creat_orders(request):
    client = Client.objects.get(pk=5)
    item = Items.objects.get(pk=1)
    order = Orders(client=client, price=100000)
    order.save()
    order.item.add(item)
    return HttpResponse("ok")



class ListItems(View):
    def get(self, request, client_id):
        client = Client.objects.filter(pk=client_id).first()

        td = timezone.now()
        last_week = td - timedelta(days=7)
        last_month = td - timedelta(days=30)
        last_year = td - timedelta(days=365)

        order_last_week = Orders.objects.filter(client_id=client_id, date_time_reg__gte=last_week)
        order_last_month = Orders.objects.filter(client_id=client_id, date_time_reg__gte=last_month)
        order_last_year = Orders.objects.filter(client_id=client_id, date_time_reg__gte=last_year)

        items_last_week = Items.objects.filter(orders__in=order_last_week).distinct()
        items_last_month = Items.objects.filter(orders__in=order_last_month).distinct()
        items_last_year = Items.objects.filter(orders__in=order_last_year).distinct()


        context = {
            'items_last_week': items_last_week,
            'items_last_month': items_last_month,
            'items_last_year': items_last_year,
            'client': client,
        }
        return render(request, 'website/list_items.html', context)
    

class ImageView(View):
    def get(self, request):
        form = ImageDownload()
        return render(request, 'website/photo.html', {'form': form})
    
    def post(self, request):
        form = ImageDownload(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            return HttpResponse("Загруза произошла успешно!")
