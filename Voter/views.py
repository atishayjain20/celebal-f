from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Voter,Group
# Create your views here.

aadhar=0
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} !')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html')
def login(request):
    if request.method=="POST":
        global aadhar
        aadhar=request.POST['Aadhar']
        aadhar=int(aadhar)
        if Voter.objects.filter(aadhar=aadhar).exists():
            v1=Voter.objects.filter(aadhar=aadhar).first()
            print(v1.contact)
            return redirect("otp")
        else:
            return redirect("home")
    return render(request,'login.html')

def otp(request):
    otp="1234"
    if request.method == "POST":
        o1=request.POST['otp']
        if o1==otp:
            return redirect("Group")
    return render(request,"otp.html")


# for the Groups 
def Gr(request):
    print(aadhar)
    if aadhar:
        v1=Voter.objects.filter(aadhar=aadhar).first()
        g1=Group.objects.filter(ward=v1.ward,city=v1.city)
    return render(request,'groups.html',{'voter':v1,"groups":g1})