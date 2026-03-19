from django.shortcuts import render
from .models import Customer
# from .models import passwordrest
import random
from django.core.mail import send_mail


# Create your views here.
def landing(request):
    return render(request, 'landing.html')

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
            msg = 'E-mail ya Employee ID already exists!'
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



def send_otp(req):                          # For sending the OTP for forgetting the Password 
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

def verify_otp(req):                     # For Verifying the OTP for forgetting the Password 
    if req.method == 'POST':
        user_otp = int(req.POST.get('otp'))
        # print(user_otp)
        session_otp = req.session.get('classotp')
        print(session_otp)
        if user_otp==session_otp:
            print("OTP Correct!")
            return render(req, 'userdash.html')
        else:
            print("OTP wrong")
            msg = 'Wrong OTP'
            return render(req, 'enterotp.html', {'msg': msg})
            # return render(req, 'enterotp.html')
    return render(req, 'verify_otp.html')

def resetpass(req):
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

        if e == 'roushanrajput12362@gmail.com' and p == '12362':
            return render(req, 'userdash.html')
        # emp = employee.objects.filter(email=e, Password=p).first()
        m= Customer.objects.filter(email=e)
        if m :
            req.session['emp_email'] = e               #session me save krne ke liye aise hm use krte h 
            return render(req, 'empdashboard.html')
        else:
            return render(req, 'login.html', {'error': 'Email ya Password galat hai'})

def Register(request):
    return render(request, 'Register.html')

def postyouradd(request):
    return render(request, 'postyouradd.html')
 
