from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class homeProduct(models.Model):
    product_id =models.AutoField(primary_key=True) 
    name = models.CharField(max_length=50,null=True)
    price = models.IntegerField(default=0)

    catagory = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=500,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank = True)
    digital = models.BooleanField(default=False,null=True, blank=True)
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    name= models.CharField(null=True, max_length=50)
    email =models.EmailField( max_length=254)
    
    def __str__(self) -> str:
        return self.name
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True,blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete =models.BooleanField(default= False)
    transaction_id = models.CharField(null=True, max_length=50)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        
        total = sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(homeProduct, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property 
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
     
    address = models.CharField(max_length=200, null=False)
    name = models.CharField( max_length=50)
    email = models.EmailField(max_length=254,default="")
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zip_code = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    phone = models.CharField( max_length=10,default="")

    def __str__(self):
	    return self.name 
 
 
 
class Contact(models.Model):
    msg_id = models.AutoField(primary_key = True)
    name= models.CharField(max_length=50)
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=10,default="")
    desc = models.CharField(max_length=500,default="")
   


    def __str__(self) -> str:
        return self.name
 