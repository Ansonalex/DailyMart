from django.shortcuts import render,redirect
from.models import*
from adminapp.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from userapp.models import*
def ind(request):
    category=CATEGORIES.objects.all().count()
    product=PRODUCTS.objects.all().count()
    contacts=CONTACTS.objects.all().count()
    registered=REG.objects.all().count()
    checkoutdata=CHECKOUT.objects.all().count()
    return render(request,"ind.html", {'category':category,'product':product,'contacts':contacts,'registered':registered,'checkoutdata':checkoutdata})
def viewreg(request):
    data=REG.objects.all()
    return render(request,"viewreg.html", {'data':data})
def addproducts(request):
    data1=CATEGORIES.objects.all()
    return render (request,"addproducts.html", {'data1':data1})
def product(request):
    if request.method=="POST":
        productname=request.POST["productname"]
        productimage=request.FILES["productimage"]
        productprice=request.POST["productprice"]
        productcat=request.POST["category"]
        data=PRODUCTS(productname=productname,productimage=productimage,productprice=productprice,category=productcat)
        data.save()
    return redirect('viewproducts')
def addcategory(request):
    return render(request,"addcategory.html")
def category(request):
    if request.method=="POST":
        categoryname=request.POST["categoryname"]
        categoryimage=request.FILES["categoryimage"]
        categorydiscription=request.POST["categorydiscription"]

        data=CATEGORIES(categoryname=categoryname,categoryimage=categoryimage,categorydiscription=categorydiscription)
        data.save()
    return redirect('viewusercategory')
def viewcategory(request):
    data=CATEGORIES.objects.all()
    return render(request,"viewcategory.html", {'data':data})

def editcategory(request,id):
    data=CATEGORIES.objects.filter(id=id)
    return render(request,"editcatagory.html",{'data':data})

def update(request,id):
    if request.method=="POST":
        categoryname=request.POST["categoryname"]
        categorydiscription=request.POST["categorydiscription"]
        try:
            img_c = request.FILES['categoryimage']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = CATEGORIES.objects.get(id=id).categoryimage

        CATEGORIES.objects.filter(id=id).update(categoryname=categoryname,categoryimage=file,categorydiscription=categorydiscription)
    return redirect("viewcategory")
def delete(request,id):
    data=CATEGORIES.objects.filter(id=id).delete()
    return redirect("viewcategory")

def viewproducts(request):
    data=PRODUCTS.objects.all()
    return render(request,"viewproducts.html", {'data':data})

def editproducts(request,id):
    data=PRODUCTS.objects.filter(id=id)
    data1=CATEGORIES.objects.all()
    return render(request,"editproduct.html",{'data':data,'data1':data1})

def update1(request,id):
    if request.method=="POST":
        productname=request.POST["productname"]
        productprice=request.POST["productprice"]
        productcat=request.POST["category"]

        try:
            img_c = request.FILES['productimage']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = PRODUCTS.objects.get(id=id).productimage

        PRODUCTS.objects.filter(id=id).update(productname=productname,productimage=file,productprice=productprice,category=productcat)
    return redirect("viewproducts")
def delete(request,id):
    data=PRODUCTS.objects.filter(id=id).delete()
    return redirect("viewproducts")
def viewcontact(request):
    data=CONTACTS.objects.all()
    return render(request,"viewcontact.html", {'data':data})
def viewcheckout(request):
    data=CHECKOUT.objects.all()
    return render(request,"viewcheckout.html", {'data':data})


# Create your views here.

    

    

# Create your views here.
