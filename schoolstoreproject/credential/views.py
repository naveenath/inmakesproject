from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .forms import SignUpForm




# Create your views here.


def register(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)

			return redirect('login')
		else:
			messages.error(request, 'Correct the errors below')
	else:
		form = SignUpForm()

	return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("logged in")
            return redirect('home')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'login.html')


# def register(request):
#     if request.method=='POST':
#
#         username=request.POST['username']
#         password=request.POST['password']
#         cpassword=request.POST['password1']
#         if password==cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, "username already exists")
#                 return redirect('register')
#             else:
#                 user=User.objects.create_user(username=username,password=password)
#                 user.save()
#                 print("user created")
#                 return redirect('login')
#
#         else:
#             print("password not matching")
#             return redirect('register')
#         return redirect('/')
#     return render(request,'register.html')
#
# class RegistrationView(View):
#     def get(self,request,*args,**kw):
#         form=RegistrationForm()
#         return render(request,'register.html',{'form':form})
#     def post(self,request,*args,**kwargs):
#         form=RegistrationForm(request.POST)
#         if form.is_valid():
#             User.objects.create_user(**form.cleaned_data)
#             messages.success(request,'account is registered')
#             return redirect('login')
#         else:
#             messages.error(request,'account is not added')
#             return render(request,'register.html',{'form':form})



def logout(request):
    auth.logout(request)
    return render(request, 'index.html')
