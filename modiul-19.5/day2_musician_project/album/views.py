from django.shortcuts import render,redirect
from .import forms
from .import models
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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
@method_decorator(login_required,name='dispatch')
class add_album_view(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name='album.html'
    success_url=reverse_lazy('home')
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Add'
        return context

    

def edit_album(request,id):
    post=models.Album.objects.get(pk=id)
    album=forms.AlbumForm(instance=post)
    if request.method=="POST" :
        album=forms.AlbumForm(request.POST,instance=post)
        if album.is_valid():
            album.save()
            return redirect('home')
   
    return render(request,'album.html',{'form':album})

@method_decorator(login_required,name='dispatch')
class edit_album_view(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name='album.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Edit'
        return context



def delete_album(request,id):
    post=models.Album.objects.get(pk=id)
    post.delete()
    return redirect('home')

@method_decorator(login_required,name='dispatch')
class delete_album_view(DeleteView):
    model = models.Album
    template_name='delete.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('home')
