from django.urls import path
from.import views
urlpatterns = [
  path('index',views.index,name="index"),          
  path('regform',views.regform,name="regform"),
  path('regforms',views.regforms,name="regform"),
  path('products/<str:category>',views.products,name="products"),
  path('viewusercategory',views.viewusercategory,name="viewusercategory"),
  path('singleproducts/<int:id>',views.singleproducts,name="singleproducts"),
  path('contact',views.contact,name="contact"),
  path('contacts',views.contacts,name="contacts"),
  path('login',views.login,name="login"),
  path('loginforms',views.loginforms,name="loginforms"),
  path('userlogout',views.userlogout,name="userlogout"),
  path('cart',views.cart,name="cart"),
  path('checkout',views.checkout,name="checkout"),
  path('cartdata/<int:id>',views.cartdata,name="cartdata"),
  path('delete1/<int:id>',views.delete1,name="delete1"),
  path('success',views.success,name="success"),
  path('checkoutdata',views.checkoutdata,name="checkoutdata"),

]
