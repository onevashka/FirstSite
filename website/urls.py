from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about_yourself/', views.about_yourself, name='about_yourself'),
    path("creat_client/", views.creat_client, name='creat_client'),
    path("creat_item/", views.creat_items, name='creat_item'),
    path('creat_order/', views.creat_orders, name='creat_orders'),
    path('items/<int:client_id>/', views.ListItems.as_view(), name='list_items'),
    path('photos/', views.ImageView.as_view(), name='photo'),
]
