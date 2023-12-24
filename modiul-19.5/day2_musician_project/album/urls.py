from django.urls import path
from .import views

urlpatterns = [
    # path('add/',views.add_album, name='album'),
    path('add/',views.add_album_view.as_view(), name='album'),
    # path('edit/<int:id>',views.edit_album, name='edit_album'),
    path('edit/<int:id>/',views.edit_album_view.as_view(), name='edit_album'),
    # path('delete/<int:id>',views.delete_album, name='delete_album'),
    path('delete/<int:id>/',views.delete_album_view.as_view(), name='delete_album'),
]