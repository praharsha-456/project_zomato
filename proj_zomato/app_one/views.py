from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    if request.method=='POST':
        name_1=request.POST['email']
        password=request.POST['psw']
        # try:
        x=UserModel.objects.get(username=name_1,password=password)
        for i in x:
            name=i.username
        y=PlaceOrderModel.objects.filter(name=name_1)
        for i in y:
            orders=i.dish_placed
        context={'my_orders':orders,'name':name}
        return render(request,'temp_one/home2.html',context)
    else:
        return render(request,'temp_one/home.html')

def signup(request):
    if request.method=="POST":
        name_1=request.POST['name']
        username_1=request.POST['email']
        password=request.POST['psw']
        print(name_1)
        print(username_1)
        user_typ=request.POST.get('usr_typ')
        
        x=UserModel.objects.filter(username=username_1)
        if x.exists():
            return render(request,'temp_one/signup.html')
        else:
            y=UserModel(name=name_1,username=username_1,password=password,user_type=user_typ)
            y.save()
            return render(request,'temp_one/signup.html')
    else:
        return render(request,'temp_one/signup.html')
