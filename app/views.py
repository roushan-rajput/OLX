from django.shortcuts import render,redirect,get_object_or_404
from .models import Customer,Product,Message
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

def reg_data(req):

    if req.method == 'POST':

        name = req.POST.get('name')
        email = req.POST.get('email')
        contact = req.POST.get('contact')
        city = req.POST.get('city')
        password = req.POST.get('password')
        cpassword = req.POST.get('cpassword')
        role = req.POST.get('role')

        existing_user = Customer.objects.filter(email=email).first()

        # UPDATE
        if existing_user:
            existing_user.name = name
            existing_user.contact = contact
            existing_user.city = city
            existing_user.role = role

            if password:
                if password == cpassword:
                    existing_user.password = password
                else:
                    return render(req, 'register.html', {
                        'msg': 'Password not match',
                        'user': existing_user
                    })

            existing_user.save()

            return render(req, 'register.html', {
                'msg': 'Profile Updated Successfully',
                'user': existing_user
            })

        # REGISTER
        else:
            if password == cpassword:
                Customer.objects.create(
                    name=name,
                    email=email,
                    contact=contact,
                    city=city,
                    password=password,
                    role=role
                )
                return render(req, 'register.html', {'msg': 'Registered Successfully'})
            else:
                return render(req, 'register.html', {'msg': 'Password not match'})

    # 🔥 THIS WAS MISSING (VERY IMPORTANT)
    return render(req, 'register.html')
    

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

        user = Customer.objects.filter(email=e, password=p).first()

        if user:
            req.session['email'] = user.email
            req.session['role'] = user.role   # 🔥 ADD THIS

            # 🔥 ROLE BASED REDIRECT
            if user.role == 'seller':
                return render(req, 'shkprdash.html')   # seller dashboard
            else:
                return render(req, 'userdash.html')    # buyer dashboard

        else:
            return render(req, 'login.html', {'error': 'Invalid credentials'})

def edit_profile(req):
    email = req.session.get('email')

    if not email:
        return redirect('login')

    user = Customer.objects.get(email=email)

    return render(req, 'register.html', {'user': user})

def shkpprofile(req):
    # 🔐 Check if user logged in
    email = req.session.get('email')

    if not email:
        return redirect('shkpdash')   # agar session nahi hai

    try:
        user = Customer.objects.get(email=email)
    except Customer.DoesNotExist:
        return redirect('login')

    return render(req, 'shkpprofile.html', {'user': user})

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

        seller_email=req.session.get('email')
        )
        print(pn,pp,pi,pr,pim,)
        return render(req, 'allproduct.html')
    items = Product.objects.all().order_by('-id')
    return render(req, 'dashboard.html', {'items': items})

def product(request):
    items = Product.objects.all()
    return render(request, 'product.html',{'items': items})

def allproduct(request):
    if request.session.get('role') == 'seller':
        items = Product.objects.filter(seller_email=request.session.get('email'))
    else:
        items = Product.objects.all()

    return render(request, 'allproduct.html', {'items': items})

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


# def chats(request):
#     return render(request, 'chat.html')

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

# def cuschats(request):
#     return render(request, 'cuschats.html')


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

    elif sort == '1000-4999':
        products = products.filter(productprice__gte=1000, productprice__lte=4999)

    elif sort == '5000plus':
        products = products.filter(productprice__gte=5000)

    else:
        print("SHOWING ALL PRODUCTS")

    print("FINAL COUNT:", products.count())

    return render(request, 'product.html', {'items': products})

def chat_page(request, other_user_email, product_id):

    # ✅ Check login
    current_user = request.session.get('email')
    if not current_user:
        return redirect('login')

    # ✅ Get product
    product = get_object_or_404(Product, id=product_id)

    # ✅ Allow only seller OR buyer
    if current_user != product.seller_email and current_user != other_user_email:
        return redirect('login')  # or show error page

    # ✅ Get other user data
    other_user = Customer.objects.filter(email=other_user_email).first()

    # =========================                     
    # ✅ SAVE MESSAGE
    # =========================
    if request.method == "POST":
        msg = request.POST.get('message')

        if msg and msg.strip():
            Message.objects.create(
                sender=current_user,
                receiver=other_user_email,
                message=msg.strip(),
                product=product   # 🔥 better FK instead of product_id
            )

        return redirect('chat_page', other_user_email=other_user_email, product_id=product.id)
    
    # =========================
    # ✅ FETCH MESSAGES
    # =========================
    messages = Message.objects.filter(
        product=product,
        sender__in=[current_user, other_user_email],
        receiver__in=[current_user, other_user_email]
    ).order_by('timestamp')

    # =========================
    # ✅ RENDER
    # =========================
    return render(request, 'chat.html', {
        'messages': messages,
        'product': product,
        'other_user': other_user,
        'current_user': current_user
    })


def chat_list(request, other_user, product_id):
    current_user = request.session.get('email')

    # अगर login नहीं
    if not current_user:
        return redirect('login')

    product = get_object_or_404(Product, id=product_id)

    # दूसरे user की details
    other_user_data = Customer.objects.filter(email=other_user).first()

    # 🔥 MESSAGE SAVE
    if request.method == "POST":
        msg = request.POST.get('message')

        if msg and msg.strip() != "":
            Message.objects.create(
                sender=current_user,
                receiver=other_user,
                message=msg,
                product_id=product_id
            )

        return redirect('chat_page', other_user=other_user, product_id=product_id)

    # 🔥 FETCH MESSAGES (MAIN FIX)
    messages = Message.objects.filter(
        product_id=product_id,
        sender__in=[current_user, other_user],
        receiver__in=[current_user, other_user]
    ).order_by('timestamp')

    return render(request, 'chat.html', {
        'messages': messages,
        'other_user': other_user,
        'product': product,
        'other_user_data': other_user_data,
        'current_user': current_user   # 🔥 IMPORTANT
    })

def userprofile(req):
    # 🔐 Check if user logged in
    email = req.session.get('email')

    if not email:
        return redirect('userdash')   # agar session nahi hai

    try:
        user = Customer.objects.get(email=email)
    except Customer.DoesNotExist:
        return redirect('login')

    return render(req, 'userprofile.html', {'user': user})

def logout_view(req):
    req.session.flush()
    return redirect('login')