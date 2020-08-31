from django.shortcuts import render , redirect
from django.contrib.auth.models import User,auth
from django.db import IntegrityError
from django.contrib.auth import authenticate , login ,logout
# Create your views here.
def onhome(request):
    return render(request,'index.html')

def donate(request):
    return render(request,'donate.html')

def user_login(request):
    if request.method == 'GET':
        return render(request, 'joinus.html')
    else:
        #picup=globals(username)
        user =authenticate(email=request.POST['Email'], password=request.POST['password'])

        if user is None:

            #auth.login(request,user)
            login(request,user)
            return redirect('/', {"param":'hi you are logged in'})
        else:
            return render(request, 'joinus.html', {'ok': 'Invalid username or password'})




def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        global username
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        last_name = request.POST['re_type_password']
        if password == last_name:
            try:
                x = User.objects.create_user(username=username, email=email, password=password)
                x.save()

                return redirect(user_login)
            except IntegrityError:
                return render(request, 'signup.html',
                              {'error': 'username has used previously please try with another one'})


        else:
            return render(request, 'signup.html', {'name': 'You entered wrong password , please try again'})

def logout(request):
    pass