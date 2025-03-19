from django.contrib import admin
from .models import *
from django.apps import apps


app_models = apps.get_app_config('Store').get_models()

for model in app_models:
    admin.site.register(model)

# admin.site.register(Product)
# admin.site.register(Customer)
# admin.site.register(Order)
# admin.site.register(OrderItem)
# admin.site.register(Tip)