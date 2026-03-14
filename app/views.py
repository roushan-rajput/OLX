from django.shortcuts import render
from .models import Customer
# from .models import passwordrest
# import random
from django.core.mail import send_mail



# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def login(request):
    return render(request, 'login.html')


def reg_data(req):
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

Your OLX account has been created.

Email: {e}
Password: {cp}

Please keep this information safe.

Thanks,
Company Team
""",
            'roushanrajput12362@gmail.com',
            [e],
            fail_silently=False
        )

        return render(req, 'userdash.html')

    return render(req, 'add_emp.html')



def Register(request):
    return render(request, 'Register.html')

def postyouradd(request):
    return render(request, 'postyouradd.html')