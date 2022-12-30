from django.contrib import admin
from .models import homeProduct,Customer,Order,OrderItem,ShippingAddress,Contact
# Register your models here.

admin.site.register(homeProduct)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Contact)