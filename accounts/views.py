from django.shortcuts import render, redirect


# Create your views here.
def login(req):
    if req.method == "POST":
        # TODO LOGIN user
    else:
        return render(req, 'accounts/login.html')


def register(req):
    if req.method == "POST":
        # TODO register user
    else:
        return render(req, 'accounts/register.html')


def dashboard(req):
    return render(req, 'accounts/dashboard.html')


def logout(req):
    return redirect('index')
