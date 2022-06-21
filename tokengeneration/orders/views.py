from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .models import order

# Create your views here.
# def gallery(request):
#     template_path = "orders/details.html"
    
#     context = {
#         "images" : [
#             "E:\\VSCODE\\Roy Projects\\samples\\canteen_blur.jpg",
#             "E:\\VSCODE\\Roy Projects\\samples\\d.jpg",
#         ]
#     }

#     return render(request, template_path,context)

def order(request):
	if request.method == 'POST':
		name = request.POST['fname']
		phno = request.POST['phno']
		item = request.POST['item']
		addons = request.POST['addons']
		models.order.objects.create(name = name, ph_no= phno,items=item, addons= addons)
		order_id = models.order.objects.get(name = name, ph_no= phno,items=item, addons= addons)
		# saveitems = order()
		# order_id.items = request.POST.get('items')
		# print(items)
		print(order_id.id)
		return render(request, 'orders/success.html', {'order_id':order_id})

	return render(request, 'orders/details.html')

def view_orders(request):
	orders_obj = models.order.objects.all()
	return render(request, 'orders/allorders.html', {'orders_obj':orders_obj})