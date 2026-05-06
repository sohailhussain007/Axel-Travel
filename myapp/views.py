from django.contrib.auth.models import User, auth
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactMessage  # ✅ Import your model
from django.conf import settings
from django.core.mail import send_mail


# ---------- Simple page render views ----------
def index(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def destinations(request):
    return render(request, 'destinations.html')

def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save message in database
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        subject = f"New Contact Message from {name}"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            # ✅ Send the visitor's message to you (admin)
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,  # from your sending Gmail
                ['sohail.hussain072002@gmail.com'],  # your receiving Gmail
                fail_silently=False,
            )

            # ✅ Auto-reply to visitor
            send_mail(
                "Thanks for contacting AxelTravel!",
                f"Hi {name},\n\nThanks for reaching out to AxelTravel. We'll get back to you soon!\n\nBest regards,\nThe AxelTravel Team",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            messages.success(request, "Thank you! Your message has been sent successfully.")
        except Exception as e:
            print("Email Error:", e)
            messages.error(request, f"Sorry, something went wrong while sending your message. ({e})")

        return redirect('contact')

    return render(request, 'contact.html')


def faq(request):
    return render(request, 'faq.html')


# ---------- Login ----------
def login(request):
    if request.method == "POST":
        usern = request.POST["username"]
        passn = request.POST["password"]

        userm = auth.authenticate(username=usern, password=passn)

        if userm is not None:
            auth.login(request, userm)
            messages.success(request, f"Welcome back, {usern}!")
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')


# ---------- Logout ----------

def logout(request):
    # Clear any old messages
    list(messages.get_messages(request))
    django_logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('login')



# ---------- Signup ----------
def signup(request):
    if request.method == "POST":
        usern = request.POST["username"]
        emails = request.POST["email"]
        passn = request.POST["password"]
        c_passn = request.POST["c_password"]
        fname = request.POST["first_name"]
        lname = request.POST["last_name"]

        if passn == c_passn:
            if User.objects.filter(email=emails).exists():
                messages.warning(request, "Email already exists.")
                return redirect("signup")
            elif User.objects.filter(username=usern).exists():
                messages.warning(request, "Username already exists.")
                return redirect("signup")
            else:
                userf = User.objects.create_user(
                    username=usern,
                    email=emails,
                    password=passn,
                    first_name=fname,
                    last_name=lname
                )
                userf.save()
                messages.success(request, "Account created successfully! Please login.")
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect("signup")
    return render(request, 'signup.html')

