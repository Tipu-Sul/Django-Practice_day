from django.shortcuts import render,redirect
from. import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def signUp(request):
    if request.method == 'POST':
        form=forms.signupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been registered")
            return redirect('login')

    else:
        form=forms.signupForm()
    return render(request, './signup.html', {'form': form ,'type':'register'})

def user_login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name,password=user_pass)
            if user is not None:    
                messages.success(request,'Successfully logged in')
                login(request,user)
                return redirect('profile')
            else:
                messages.warning(request,'please enter valid information or register yoursself')
                return redirect('signup')
    else:
        form=AuthenticationForm()
    return render(request, 'signup.html', {'form': form,'type':'login'})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def editProfile(request):
    if request.method == 'POST':
        profileForm=forms.changeUserData(request.POST,instance=request.user)
        if profileForm.is_valid():
            profileForm.save()
            messages.success(request,'Account successfully updated')
            return redirect('profile')
        
    else: 
        profileForm=forms.changeUserData(instance=request.user)
    return render(request, 'signup.html', {'form': profileForm,'type':'Edit_Profile'})

def passChange(request):
    if request.method == 'POST':
        form=PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password successfully updated')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request, 'passChange.html',{'form': form,'type':'Edit_Password'}) 

def passChange2(request):
    if request.method == 'POST':
        form=SetPasswordForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password successfully updated')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form=SetPasswordForm(user=request.user)
    return render(request, 'passChange.html',{'form': form , 'type': 'Password change'})

def user_logout(request):
    logout(request)
    messages.success(request,'You are logged out successfully ')
    return redirect('login')    






    


