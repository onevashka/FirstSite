from django.contrib import admin
from .models import Client, Items, Orders

@admin.action(description='Сбросить кол-во в ноль!')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date_time_reg']
    list_filter = ['date_time_reg', 'name']
    search_fields = ['name', 'email', 'phone']
    search_help_text = 'Поиск по имени, почте, телефону' 


class ItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'quantity']
    list_filter = ['quantity', 'price', 'name']
    search_fields = ['name', 'price',]
    search_help_text = 'Поиск по названию, цене'
    actions = [reset_quantity]
    fieldsets = [

        (

            None,
            {

                'classes': ['wide'],
                'fields': ['name'],

            },

        ),
        (

            'Подробности',
            {

                'classes': ['collapse'],
                'description': 'подробное описание',
                'fields': ['description'],

            },

        ),
        (

            'Цена и количество',
            {

                'fields': ['price', 'quantity'],

            },

        ),
]

admin.site.register(Client, ClientAdmin)

admin.site.register(Items, ItemsAdmin)
