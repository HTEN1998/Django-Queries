from django.shortcuts import render
from django.db import connection
from .models import Orders,Customers
# Create your views here.
def orders_view(request):
    if request.method=='GET':
        return render(request,'index.html')
    else:
        order_id = int(request.POST['oid'])
        cust_id = int(request.POST['cid'])
        amount = int(request.POST['amt'])

        cust_id2 = int(request.POST['cust_id'])
        cust_name = request.POST['cust_name']
        cust_location = request.POST['cust_loc']
        
        orders_obj = Orders(order_id=order_id,customer_id=cust_id,price=amount)
        # orders_obj =Orders.objects.raw('INSERT INTO demoapp_orders values({},{},{})'.format(order_id,cust_id,amount))
        orders_obj.save()
        customer_obj = Customers(customer_id=cust_id2,customer_name=cust_name,customer_loc=cust_location)
        # customer_obj = Customers.objects.raw('INSERT INTO demoapp_customers values({},{},{})'.format(cust_id2,cust_name,cust_location))
        customer_obj.save()

        output = Orders.objects.all()
        # output = Orders.objects.raw('SELECT * FROM demoapp_orders')
        output2 = Customers.objects.all()
        # output2 = Customers.objects.raw('SELECT * FROM demoapp_customers')
        
        cursor = connection.cursor()
        cursor.execute('SELECT demoapp_orders.order_id, demoapp_customers.customer_name FROM demoapp_orders INNER JOIN demoapp_customers ON demoapp_orders.customer_id = demoapp_customers.customer_id')
        join_obj = Customers.objects.filter('SELECT')

        return render(request,'output.html',{'order':output,'customer':output2,'joindata':join_obj})
        
