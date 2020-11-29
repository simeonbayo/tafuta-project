from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pass1 = form.cleaned_data.get('password1')
            pass2 = form.cleaned_data.get('password2')
            fname = form.cleaned_data.get('firstname')
            lname = form.cleaned_data.get('lastname')
            email = form.cleaned_data.get('email')
            telephone_no = form.cleaned_data.get('telephone_no')
            address = form.cleaned_data.get('address')
            district = form.cleaned_data.get('district')
            user = authenticate(username = username, password = pass1)
            login(request, user)

            return redirect('usersearch')
    else:
        form = SignUpForm
    return render(request, 'main/baseone.html', {'form': form})

