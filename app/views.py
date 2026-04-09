from django.shortcuts import render,redirect,get_object_or_404
from .models import Customer,Product
# from .models import passwordrest
import random
from django.core.mail import send_mail

  

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def shkprdash(request):
    return render(request, 'shkprdash.html')

def login(request):
    return render(request,'login.html')

def reg_data(req):                                       #Registration Data 
    if req.method == 'POST':
        n = req.POST.get('name')
        e = req.POST.get('email')
        co = req.POST.get('contact')
        ci = req.POST.get('city')
        p = req.POST.get('password')
        cp = req.POST.get('cpassword')

        # Duplicate check
        if Customer.objects.filter(email=e).exists() or Customer.objects.filter(password=p).exists():
            msg = 'E-mail already exists!'
            return render(req, 'Register.html', {'msg': msg})

        # Save to database
        Customer.objects.create(
        name=n,
        email=e,
        contact=co,
        city=ci,
        password=p,
        cpassword=cp
        )
        print(n,e,co,ci,p,cp)

        # Send email
        send_mail(
        'Company Login Details',
        f"""Hello {n},

Your OLX Pro account has been created.

Email: {e}
Password: {cp}

Please keep this information safe.

Thanks,
OLX Pro Team
""",
            'roushanrajput12362@gmail.com',
            [e],
            fail_silently=False
        )

        return render(req, 'login.html')

    return render(req, 'Register.html')

def forgetpage(request):
    return render(request, 'forgetpage.html')


def send_otp(req):                                     # For sending the OTP for forgetting the Password 
    if req.method == 'POST':
        e = req.POST.get('email')
        req.session['email']=e

        otp = random.randint(1111, 9999)
        req.session['classotp'] =otp
        send_mail(
            'OTP Verification',
            f'Generate OTP for django app is {otp}',
            'roushanrajput12362@gmail.com',
            [e]
        )
        return render(req, 'enterotp.html')
    return render(req, 'forgetpage.html')

def enterotp(request):
    return render(request, 'enterotp.html')

def verify_otp(req):                                   # For Verifying the OTP for forgetting the Password 
    if req.method == 'POST':
        user_otp = int(req.POST.get('otp'))
        # print(user_otp)
        session_otp = req.session.get('classotp')
        print(session_otp)
        if user_otp==session_otp:
            print("OTP Correct!")
            return render(req, 'shkprdash.html')
        else:
            print("OTP wrong")
            msg = 'Wrong OTP'
            return render(req, 'enterotp.html', {'msg': msg})
            # return render(req, 'enterotp.html')
    return render(req, 'verify_otp.html')

def resetpass(req):                                      # For reset the password
    if (req.method=='POST'):
        p=req.POST.get('Reset_pass')
        cp=req.POST.get('Reset_cpass')
        e=req.session['email']
        print(e)
               
        print(p,cp)
        if p==cp:
            emp_details=Customer.objects.get(email=e)
            print(emp_details.name)

def logindata(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('pass')

        # 🔹 Step 1: Admin check
        if e == 'roushanrajput12362@gmail.com' and p == '12362':
            return render(req, 'shkprdash.html')

        # 🔹 Step 2: Database check (email + password BOTH)
        emp = Customer.objects.filter(email=e, password=p).first()

        if emp:
            req.session['emp_email'] = e
            return render(req, 'userdash.html')
        else:
            return render(req, 'login.html', {'error': 'Email ya Password galat hai'})

def Register(request):
    return render(request, 'Register.html')

def add_product(request):
    return render(request, 'add_product.html')

def add_pro(req):                                        #For Add the Product 
    if req.method == 'POST':
        pn = req.POST.get('productname')
        pp = req.POST.get('productprice')
        pi = req.POST.get('productissue')
        pr = req.POST.get('productreason')
        pim = req.FILES.get('productimg')

        Product.objects.create(
        productname=pn,
        productprice=pp,
        productissue=pi,
        productreason=pr,
        productimg=pim,
        )
        print(pn,pp,pi,pr,pim)
        return render(req, 'allproduct.html')
    items = Product.objects.all().order_by('-id')
    return render(req, 'dashboard.html', {'items': items})

def product(request):
    items = Product.objects.all()
    return render(request, 'product.html',{'items': items})

def allproduct(request):
    items = Product.objects.all()
    return render(request, 'allproduct.html',{'items': items})


def edit_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'add_product.html', {'data': product})

def update_product(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == "POST":
        product.productname = request.POST.get('productname')
        product.productprice = request.POST.get('productprice')
        product.productissue = request.POST.get('productissue')
        product.productreason = request.POST.get('productreason')

        # Image update (optional)
        if request.FILES.get('productimg'):
            product.productimg = request.FILES.get('productimg')

        product.save()
        return redirect('allproduct')
    
def delete_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    product.delete()
    return redirect('allproduct')


def chats(request):
    return render(request, 'chats.html')

def profile(request):
    return render(request, 'profile.html')

def postyouradd(request):
    return render(request, 'postyouradd.html')


def logout(req):
    return render(req,'landing.html')

def buy_now(request):
    return render(request, 'product.html')

def chat(request):
    return render(request, 'product.html')


def sort(request):
    products = Product.objects.all()
    sort = request.GET.get('sort')

    print("SORT VALUE:", sort)

    # ✅ CATEGORY TYPE FILTER (using productname)
    if sort in ['phones', 'laptop', 'car', 'house']:
        products = products.filter(productname__icontains=sort)

    # ✅ PRICE FILTER
    elif sort == '0-999':
        products = products.filter(productprice__gte=0, productprice__lte=999)

    elif sort == '1000-5000':
        products = products.filter(productprice__gte=1000, productprice__lte=5000)

    elif sort == '5000plus':
        products = products.filter(productprice__gte=5000)

    else:
        print("SHOWING ALL PRODUCTS")

    print("FINAL COUNT:", products.count())

    return render(request, 'product.html', {'items': products})