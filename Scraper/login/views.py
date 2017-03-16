from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


def user_account(request):
    ''' User account page or login page '''
    if request.user.is_authenticated():
        if request.user.is_active():
            # Account dashboardlogin
            return render(request, 'login/account.html')

        else:
            # Account needs to be activated
            return render(request, 'login/activate.html')
    else:
        # Login page
        return render(request, 'login/login.html')


def user_login(request):
    ''' Logs user in '''
    uname = request.POST['login-name']
    upass = request.POST['login-passwd']


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
