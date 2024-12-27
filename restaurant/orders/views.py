from django.shortcuts import redirect, render, get_object_or_404

from orders.forms import OrderForm
from orders.models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'orders/product_list.html', {'products':products})

def place_order(request):
    product_id = request.GET.get('product_id')
    product  = None
    if product:
        product = get_object_or_404(Product, id = product_id)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')
    else:
        form = OrderForm(initial={"product":product})
    return render(request, 'orders/place_order.html', {"form":form})
        
def order_success(request):
    return render(request, 'orders/order_success.html')