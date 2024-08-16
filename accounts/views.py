from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth




#=========================================== LOGIN =================================



def login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username = username, password = password)
        # auth.authenticate returns an object if the the username and password(input by the user) 
        # are present in the db. Otherwise it'll return None.

        if user is not None:

            auth.login(request, user)    # session create horha hai
            return redirect("todo")
        
        else:

            context = {
                "invalid": "Invalid login credentials. Please check your username and password and try again."
            }

            return render(request, "accounts/login.html", context)
        
    return render(request, "accounts/login.html")



# ========================================== SIGNUP =================================



def signup(request):

    if request.method == "POST":

        new_username = request.POST.get("username")
        new_password = request.POST.get("password1")
        confirm_password = request.POST.get("password2")

        if new_password == confirm_password:

            new_user = User(
                username = new_username
            )

            new_user.set_password(new_password)
            new_user.save()

            return redirect("login")

        else:
            
            context = {
                "invalid": "Please make sure the 'Password' and 'Confirm Password' fields match."
            }

            return render(request, "accounts/signup.html", context)


    return render(request, "accounts/signup.html")    



# ========================================== LOGOUT =================================


def logout(request):

    auth.logout(request)

    return redirect("home")




