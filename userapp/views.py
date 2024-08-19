from django.shortcuts import render,redirect
from.models import*
from adminapp.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models.aggregates import Sum
def index(request):
    data=PRODUCTS.objects.all()
    data1=CATEGORIES.objects.all()
    return render(request,"index.html",{'data':data,'data1':data1})

def products(request,category):
     if category=="all":
         data=PRODUCTS.objects.all()
     else:
         data=PRODUCTS.objects.filter(category=category)
     data1=CATEGORIES.objects.all()

     
     return render(request,"products.html", {'data':data,'data1':data1})
def viewusercategory(request):
    data=CATEGORIES.objects.all()
    return render(request,"category.html",{'data':data})
def singleproducts(request,id):
    data=PRODUCTS.objects.filter(id=id)
    return render(request,"singleproducts.html", {'data':data})
def contact(request):
    return render(request,"contact.html")
def contacts(request):
    if request.method=="POST":
        Name=request.POST["Name"]
        EmailAddress=request.POST["EmailAddress"]
        Phonenumber=request.POST["Phonenumber"]
        Address=request.POST["Address"]
        data=CONTACTS(Name=Name,EmailAddress=EmailAddress,Phonenumber=Phonenumber,Address=Address)
        data.save()
    return redirect('contact')
def login(request):
    return render(request,"login.html")
def regform(request):
    return render(request,"regform.html")
def regforms(request):
    if request.method=="POST":
        Username=request.POST["Username"]
        EmailAddress=request.POST["EmailAddress"]
        Password=request.POST["Password"]
        ConfirmPassword=request.POST["ConfirmPassword"]
        data=REG(Username=Username,EmailAddress=EmailAddress,Password=Password,ConfirmPassword=ConfirmPassword)
        data.save()
    return redirect(regform)
def loginforms(request):
    if request.method == "POST":
        emailaddress=request.POST.get('EmailAddress')
        password=request.POST.get('Password')
        if REG.objects.filter(EmailAddress=emailaddress,Password=password).exists():
           data = REG.objects.filter(EmailAddress=emailaddress,Password=password).values('id','Username','ConfirmPassword').first()
           request.session['u_id'] = data['id']
           request.session['emailaddress_u'] = emailaddress
           request.session['password_u'] = password
           request.session['name'] = data['Username']
           return redirect('index') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('login')
def userlogout(request):
    del request.session['u_id']
    del request.session['emailaddress_u']
    del request.session['password_u']
    return redirect('login')
def cart(request):
    u=request.session.get('u_id')
    data=CART.objects.filter(userid=u,status=0)
    t=CART.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,"cart.html",{'data':data,'t':t})
def checkout(request):
     u=request.session.get('u_id')
     data=CART.objects.filter(userid=u,status=0)
     return render(request,"checkout.html")
def cartdata(request,id):
    if request.method=="POST":
        userid=request.session.get('u_id')
        quantity=request.POST['quantity']
        total=request.POST['total']
        data=CART(userid=REG.objects.get(id=userid),productid=PRODUCTS.objects.get(id=id),quantity=quantity,total=total,)
        data.save()
    return redirect('cart')
def delete1(request,id):
    data=CART.objects.filter(id=id).delete()
    return redirect("cart")
def success(request):
    return render(request,"success.html")
def checkoutdata(request):
    if request.method=="POST":
        userid=request.session.get('u_id')
        country=request.POST['country']
        address=request.POST['address']
        city=request.POST['city']
        zip=request.POST['zip']
        order=CART.objects.filter(userid=userid,status=0)

        for i in order:
            data=CHECKOUT(userid=REG.objects.get(id=userid),cartid=CART.objects.get(id=i.id),address=address,city=city,country=country,postalzip=zip)
            data.save()
            CART.objects.filter(id=i.id).update(status=1)
            return redirect("success")
        



# Create your views here.
