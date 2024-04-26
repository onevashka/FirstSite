from django.db import models




class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_time_reg = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def creat_client(name, email, phone, address):
        client = Client(name=name, email=email, phone=phone, address=address)
        client.save()

    def delet_client(self, name):
        client = Client.objects.filter(name=name).first()
        client.delete()

    def read_client_data(self, name):
        client = Client.objects.filter(name=name).first()
        return client

    def __str__(self) -> str:
        return f"Name client: {self.name}\nEmail client: {self.email}\nAddress client: {self.address}\nPhone number client: {self.phone}"


class Items(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_time_reg = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='photos/', default='')

    @staticmethod
    def creat_item(name, description, price, quantity):
        item = Items(name=name, description=description, price=price, quantity=quantity)
        item.save()

    def delet_item(self, name):
        item = Items.objects.filter(name=name).first()
        item.delete()

    def read_item_data(self, name):
        item = Items.objects.filter(name=name).first()
        return item
    
    def update_item(self, name, description=None, price=None, quantity=None):
        item = Items.objects.filter(name=name).first()
        if description:
            item.description = description
        if price:
            item.price = price
        if quantity:
            item.quantity = quantity
        item.save()

    def __str__(self) -> str:
        return f"Product name: {self.name}| Price: {self.price}\nProduct quantity: {self.quantity}\n---Product description---\n{self.description} "


class Orders(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=3)
    item = models.ManyToManyField(Items)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_time_reg = models.DateTimeField(auto_now_add=True)

    def set_items(self, items):
        self.items.set(items)
        self.update_price()

    def add_item(self, item):
        self.items.add(item)
        self.update_price()

    def update_price(self):
        total_price = sum(item.price for item in self.item.all())
        self.price = total_price if total_price is not None else 0
        self.save()

    def __str__(self) -> str:
        return f"Client name: {self.client.name}"