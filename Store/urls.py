from django.urls import path
from . import views
urlpatterns = [
#path('',views.home,name='home'),
#path('index',views.home,name="Store"),
    path('index',views.store,name="Store"),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('login',views.loginPage, name='login'),
    path('register',views.registerPage,name='register'),
    path('update_item/',views.update, name='update'),
    path('logout',views.logoutPage,name='logout'),
    path('product-detail/<int:id>',views.product_detail,name='product-detail'),
    path('search',views.searched,name='search'),
    path('category/<int:id>', views.category_view),
]