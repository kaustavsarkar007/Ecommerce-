from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import *
import json
import datetime
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# Create your views here.
def home(request): 
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
		#Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
        
        
    products = homeProduct.objects.all()
    print(products)
    params = {'products':products,'cartItems':cartItems}
    return render(request, 'home/home.html',params)

   
def contact(request):
    return HttpResponse("This is contact")

def about(request): 
    return HttpResponse('This is about')

def cart(request): 
    if request.user.is_authenticated:
        customer = request.user.customer
        order ,created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        
    
    else:
        items= []
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
    context ={'items':items ,'order':order}    
    return render(request,'home/cart.html',context)

def checkout(request): 
    if request.user.is_authenticated:
        customer = request.user.customer
        order ,created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        
    
    else:
        items= []
        order = {'get_cart_total':0,'get_cart_items':0}
    context ={'items':items ,'order':order}    
    

    return render(request,'home/checkout.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']    
    action = data['action'] 
    print('Action:',action)   
    print('productId:',productId) 
    
    customer = request.user.customer
    product = homeProduct.objects.get(product_id=productId)  
    order ,created = Order.objects.get_or_create(customer=customer,complete = False)
    orderItem ,created = OrderItem.objects.get_or_create(order=order,product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity-1)

    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()

        
    return JsonResponse ('Item was added',safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    #data = json.loads(request.body)

    if request.user.is_authenticated and request.method == 'POST':
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order.transaction_id = transaction_id
       
        name = request.POST.get('name','')
        customer = request.POST.get('customer')
        order = request.POST.get('order')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address1','')  + request.POST.get('address2','')
        city = request.POST.get('city','') 
        state = request.POST.get('state','') 
        zip_code = request.POST.get('zip_code','') 

        detail = ShippingAddress(customer=customer ,name=name, email=email, phone=phone, address=address,city=city,state=state,zip_code=zip_code)
        detail.save()
        
    return redirect('home')


def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method == 'POST':
        
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,'home/contact.html')


def handleSignup(request):
    #messages.success(request, 'Your query is noted. We will contact you soon')
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if len(username)>10:
            messages.error(request,"Your username must under 10 characters")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request,"Your username must a alphanumeruic characters")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request,"Password donot match")
            return redirect('home')
            
      
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('home')
        
    else:
        return HttpResponse("404 Not Found")
    
def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        user = authenticate(username=loginusername, password=loginpassword)
        
        if user is not None:
            login(request,user)
            messages.success(request, "Succesfully Login")
            return redirect('home')
        else:
            messages.error(request,"Invlid Credentials, Please try again")
            return redirect('home')
            
    return HttpResponse("404 - Not Found")

def handleLogout(request):
    
    logout(request)
    messages.success(request,"Logged out succesfully")
    return redirect('home')
