from django.urls import path
from.import views

urlpatterns = [
    path('ind',views.ind,name="ind"), 
    path('viewreg',views.viewreg,name="viewreg"),
    path('addproducts',views.addproducts,name="addproducts"),
    path('product',views.product,name="product"),
    path('addcategory',views.addcategory,name="addcategory"),
    path('category',views.category,name="category"),
    path('viewcategory',views.viewcategory,name="viewcategory"),
    path('editcategory/<int:id>/',views.editcategory,name="editcategory"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('viewproducts',views.viewproducts,name="viewproducts"),
    path('editproducts/<int:id>/',views.editproducts,name="editproducts"),
    path('update1/<int:id>/',views.update1,name="update1"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('viewcontact',views.viewcontact,name="viewcontact"),
    path('viewcheckout',views.viewcheckout,name="viewcheckout")
    


]
