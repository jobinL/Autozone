from django.contrib import admin
from .models import Category,Ecustomer,Product,Order

# Register your models here.
admin.site.register(Category)
admin.site.register(Ecustomer)
admin.site.register(Product)
admin.site.register(Order)