from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view()
def DishAPIView(request,rest):
    rest=rest.replace('_',' ')
    x=DishModel.objects.all()
    data=[]
    dishes=[]
    dishes_price=[]
    for i in x:
        if rest in i.rest_available:
            data.append({'restaurant': rest,'dish_name':i.dish_name,'dish_price':i.dish_price})
    return Response(data)

@api_view(['POST'])
@csrf_exempt
def SaveDetailsAPI(request):
    dishes=request.POST.getlist('dish')
    name=request.POST.get('name')
    rest=request.POST.get('restaurant')
    price=0
    for i in dishes:
        x=DishModel.objects.filter(dish_name=i)
        for j in x:
            price+=j.dish_price
    dishes1=','.join(dishes)
    y=PlaceOrderModel(user_order=name,rest_placed=rest,dish_placed=dishes1,total_price=price)
    y.save()
    data={'user':name,'restaurant':rest,'dishes':dishes,'total_price':price}
    return Response(data)

def home(request):
    if request.method=='POST':
        try:
            user_typ=request.POST['usr_typ']
            print(user_typ)
            if user_typ=='Customer':
                name_1=request.POST.get('email')
                password=request.POST.get('psw')
                try:
                    x=UserModel.objects.get(username=name_1,password=password,user_type=user_typ)
                    name=x.name
                    y=RestaurantModel.objects.all()
                    context={'name':name,'rest_list':y}
                    return render(request,'temp_one/home2.html',context)
                except Exception as e:
                    message_zip=zip(['warning'],['Login Error. Please sign up if you haven\'t registered'])
                    return render(request,'temp_one/home.html',{'message_zip':message_zip})
            else:
                name_1=request.POST.get('email1')
                password=request.POST.get('psw1')
                address=request.POST.get('address')
                print(name_1,password)
                try:
                    a=UserModel.objects.get(username=name_1,password=password,user_type=user_typ)
                    rest_name=a.name
                    print(rest_name)
                    x=PlaceOrderModel.objects.filter(rest_placed=rest_name)
                    print(x)
                    x1=[]
                    for i in x:
                        dishes=i.dish_placed
                        try:
                            dishes=dishes.replace('\'','').replace('"','')
                            dishes=dishes.strip("][").split(",")
                            dishes=','.join(dishes)
                        except:
                            pass
                        x1.append(dishes)
                    try:
                        print('inside if')
                        return render(request,'temp_three/rest_acc.html',{'data':zip(x,x1),'rest_name':rest_name})
                    except:
                        return render(request,'temp_three/rest_acc.html',{'rest_name':rest_name})
                except:
                    return render(request,'temp_one/home.html')
        except:
            return render(request,'temp_one/home.html')
    else:
        return render(request,'temp_one/home.html')
##RESTAURANT ACCOUNT VIEW
def RestaurantAccView(request):
    rest=request.POST['restaurant']
    x=PlaceOrderModel.objects.filter(rest_placed=rest)
    if x.exists():
        return render(request,'temp_three/rest_acc.html',{'data':x})
def signup(request):
    if request.method=="POST":
        user_typ=request.POST.get('usr_typ')
        if user_typ=='Customer':
            name_1=request.POST['name']
            username_1=request.POST['email']
            password=request.POST['psw']
        else:
            name_1=request.POST['name1']
            username_1=request.POST['email1']
            password=request.POST['psw1']
            address=request.POST['address']
        try:
            if name_1=='' or username_1=='' or password=='' or address=='':
                return redirect('sign-up')
        except:
            if name_1=='' or username_1=='' or password=='':
                return redirect('sign-up')
        print(name_1)
        print(username_1)
        x=UserModel.objects.filter(username=username_1,user_type=user_typ)
        if x.exists():
            message_zip=zip(['warning'],['User already exists, please login'])
            return render(request,'temp_one/home.html',{'message_zip':message_zip})
        else:
            y=UserModel(name=name_1,username=username_1,password=password,user_type=user_typ)
            if user_typ=='Restaurant':
                z=RestaurantModel(rest_name=name_1,rest_address=address)
                z.save()
            y.save()
            message_zip=zip(['success'],['Your account has been registered. Please sign in now'])
            return render(request,'temp_one/home.html',{'message_zip':message_zip})
    else:
        return render(request,'temp_one/signup.html')


def my_orders(request,name1):
    # if request.method=="POST":
    x=PlaceOrderModel.objects.filter(user_order=name1)
    orders_list=[]
    restaurants_list=[]
    price_list=[]
    date_time_list=[]
    for i in x:
        orders=i.dish_placed
        orders=orders.replace('\'','').replace('"','')
        orders=orders.strip("][").split(",")
        orders=','.join(orders)
        restaurants=i.rest_placed
        price=i.total_price
        price_list.append(price)
        date_time=i.date
        orders_list.append(orders)
        restaurants_list.append(restaurants)
        date_time_list.append(date_time)
    print(orders_list)
    context={'ordered_zip':zip(orders_list,restaurants_list,price_list,date_time_list),'name':name1}
    return render(request,'temp_one/orders.html',context)
    # else:
    #     return render(request,'temp_one/home.html')

def RestaurantView(request):
    if request.method=="POST":
        rest=request.POST.get('restaurant')
        user=request.POST.get('name')
        print(user)
        x=DishModel.objects.all()
        dish_list=[]
        price_list=[]
        for i in x:
            if rest in i.rest_available:
                dish=i.dish_name
                price=i.dish_price
                dish_list.append(dish)
                price_list.append(price)
        y=RestaurantModel.objects.get(rest_name=rest)
        address=y.rest_address
        context={'dish_n_price_list':zip(dish_list,price_list),'name':user,'restaurant':rest,'address':address}
        return render(request,'temp_two/restaurant.html',context)
    else:
        return redirect('home')
@csrf_exempt
def PlaceOrderView(request):
    if request.method=='POST':
        dishes=request.POST.getlist('dish')
        name=request.POST.get('name')
        rest=request.POST.get('restaurant')
        price=0
        print(dishes)
        for i in dishes:
            x=DishModel.objects.filter(dish_name=i)
            for j in x:
                price+=j.dish_price
        dishes1=','.join(dishes)
        y=PlaceOrderModel(user_order=name,rest_placed=rest,dish_placed=dishes1,total_price=price)
        y.save()
        return redirect('home')
    else:
        return redirect('home')

def AllOrders(request):
    print(PlaceOrderModel.objects.all())
    return render(request,'temp_two/allorders.html',{'details':'x'})
def AddItem(request,name1):
    name1=name1.replace('_',' ')
    if request.method=='POST':
        item_name=request.POST.get('item_name')
        item_price=request.POST.get('item_price')
        try:
            x=DishModel.objects.filter(dish_name=item_name)
            print(x)
            n=''
            if x.exists():
                for i in x:
                    if name1 in i.rest_available:
                        n+='1'
                        break
                    else:
                        n=''
                        val=x.rest_available
                        x.update(rest_available=val+','+name1)
                if n=='':
                    return redirect('add-items')
                else:
                    message='This item has already been added'
                    return render(request,'temp_three/add_items.html',{'rest_name':name1,'message':message})
            else:
                x=DishModel(dish_name=item_name,dish_price=item_price,rest_available=name1)
                x.save()
                message='The item has been added'
                return render(request,'temp_three/add_items.html',{'rest_name':name1,'message':message})
        except:
            print('o')
            x=DishModel(dish_name=item_name,dish_price=item_price,rest_available=name1)
            x.save()
            message='The item has been added'
            return render(request,'temp_three/add_items.html',{'rest_name':name1,'message':message})
    else:
        return render(request,'temp_three/add_items.html',{'rest_name':name1})