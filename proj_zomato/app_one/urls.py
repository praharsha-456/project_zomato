from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('sign_up/',views.signup,name='sign-up'),
    path('restaurant/',views.RestaurantView,name='restaurant'),
    path('order_placed/',views.PlaceOrderView,name='order-placed'),
    path('restaurant/<str:rest>/',views.DishAPIView),
    path('save-details/',views.SaveDetailsAPI,name='details-api'),
    path('<str:name1>-orders/',views.my_orders,name='orders'),
    path('all-orders/',views.AllOrders,name='all-orders'),
    path('<str:name1>/add-items/',views.AddItem,name='add-items')
]