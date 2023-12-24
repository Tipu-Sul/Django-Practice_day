from django.shortcuts import render,redirect
from .import forms
from .import models


# Create your views here.
def add_album(request):
    if request.method=="POST" :
        album=forms.AlbumForm(request.POST)
        if album.is_valid():
            album.save()
            return redirect('album')
    else:
        album=forms.AlbumForm()
    return render(request,'album.html',{'form':album})


def edit_album(request,id):
    post=models.Album.objects.get(pk=id)
    album=forms.AlbumForm(instance=post)
    if request.method=="POST" :
        album=forms.AlbumForm(request.POST,instance=post)
        if album.is_valid():
            album.save()
            return redirect('home')
   
    return render(request,'album.html',{'form':album})

def delete_album(request,id):
    post=models.Album.objects.get(pk=id)
    post.delete()
    return redirect('home')


