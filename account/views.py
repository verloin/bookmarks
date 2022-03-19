from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from account.forms import LoginForm


def user_login(request):
    user = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request,
                  'login.html', {
                      'form': form})