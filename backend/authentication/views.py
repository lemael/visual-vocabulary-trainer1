from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from authentication.forms import SignInForm, SignUpForm

from .token import genenratorToken

#from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
  return render(request, 'app/home.html')

def register(request):
  if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            user = fm.save(commit=False)
            messages.success(request, 'Account created successfully')
            fm.is_active = False
            fm.save()

            # send a welcome email
            subject = "Welcome to Mael Pro System Authentication"
            message = "Welcome"+ user.first_name + "" + user.last_name
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=False)
            # Confirmation Email
            current_site = get_current_site(request) #link of site
            email_subject = 'Please Activate Your Account'
            messageConfirm = render_to_string("emailConfirm.html", {
                'name': fm.cleaned_data.get('name'),
                'domain': current_site.domain,
                'uid': fm.cleaned_data.get('id'),
                'token': genenratorToken.make_token(user),

            }) 

            email = EmailMessage(
                email_subject,
                messageConfirm,
                settings.EMAIL_HOST_USER,
                [fm.cleaned_data.get('email')],
            )

            email.fail_silently = False
            email.send()
            return redirect('login')
  else:
        fm = SignUpForm()
    
  return render(request, 'app/register.html', {'form':fm, 'show_home_button': True})

def logIn(request):
    my_user = None  # Initialiser my_user avec None

    if request.method == "POST":
        fm = SignInForm(request, data=request.POST)
        if fm.is_valid():
            my_user = User.objects.get(username=fm.cleaned_data.get('username'))
            if my_user.is_active:
                user = fm.get_user()
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Sorry, you have not confirmed your email address.")
        else:
            fm = SignInForm()
    else:
        fm = SignInForm()

    return render(request, 'app/login.html', {'form': fm, 'show_home_button': True})



def logOut(request):
  logout(request)
  messages.success(request, 'You have been disconnected')
  return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserWarning):
        user = None 

    if user is not None and genenratorToken.check_token(user, token):
        user.is_active= True
        user.save()
        messages.success(request,"Your account has been activated. Congratulations!")
        return redirect('login')
    else:
        messages.error(request, 'Activation failed!!')
        return redirect('home')
