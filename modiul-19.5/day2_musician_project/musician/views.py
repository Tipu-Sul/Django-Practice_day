from django.shortcuts import render,redirect
from .import forms
from .import models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.d
def register_user(request):
    if request.method =='POST':
        register_form=forms.registration_form(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "User registration successful")
            return redirect('login')
    else:
        register_form=forms.registration_form()
    return render(request, 'signup.html', {'form': register_form, 'type':'Register'})

def user_login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request, "User login successful")
                login(request,user)
                return redirect('musician')
            else:
                messages.warning(request, "User information not fund,signup at first")
                return redirect('signup')
    else:
        form=AuthenticationForm()
    return render(request,'signup.html', {'form': form,'type':"Login"})

class user_login_view(LoginView):
    template_name='signup.html'
    # success_url=reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request,'User login successful')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request,'User login information incorrect')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='login'
        return context


@login_required
def add_musician(request):
    if request.method =='POST':
        musician=forms.MusicianForm(request.POST)
        if musician.is_valid():
            musician.save()
            return redirect('musician')
    else:
        musician=forms.MusicianForm()
    return render(request, 'musician.html', {'form':musician})

@method_decorator(login_required,name='dispatch')
class add_musician_view( CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name='musician.html'
    success_url=reverse_lazy('musician')
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Add'
        return context

    


@login_required
def edit_musician(request,id):
    post=models.Musician.objects.get(pk=id)
    musician=forms.MusicianForm(instance=post)
    if request.method =='POST':
        musician=forms.MusicianForm(request.POST,instance=post)
        if musician.is_valid():
            musician.save()
            return redirect('home')
   
    return render(request, 'musician.html', {'form':musician})
@method_decorator(login_required,name='dispatch')
class edit_musician_view(UpdateView):
    model = models.Musician
    form_class=forms.MusicianForm
    template_name='musician.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Edit'
        return context



def user_logout(request):
    logout(request)
    messages.success(request,'logged out successfully')
    return redirect('login')

class user_logout_view(LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')



