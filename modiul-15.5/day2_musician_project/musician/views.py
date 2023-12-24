from django.shortcuts import render,redirect,get_object_or_404
from .import forms
from .import models

# Create your views here.d
def add_musician(request):
    if request.method =='POST':
        musician=forms.MusicianForm(request.POST)
        if musician.is_valid():
            musician.save()
            return redirect('musician')
    else:
        musician=forms.MusicianForm()
    return render(request, 'musician.html', {'form':musician})


def edit_musician(request,id):
    post=models.Musician.objects.get(pk=id)
    # post=get_object_or_404(models.Musician,pk=id) 
    musician=forms.MusicianForm(instance=post)
    if request.method =='POST':
        musician=forms.MusicianForm(request.POST,instance=post)
        if musician.is_valid():
            musician.save()
            return redirect('home')
   
    return render(request, 'musician.html', {'form':musician})