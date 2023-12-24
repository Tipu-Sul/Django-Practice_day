from django.urls import path
from .import views

urlpatterns = [
    path('singup/',views.register_user, name='signup'),
    # path('login/',views.user_login, name='login'),
    path('login/',views.user_login_view.as_view(), name='login'),
    # path('logout/',views.user_logout, name='logout'),
    path('logout/',views.user_logout_view.as_view(), name='logout'),
    # path('add/',views.add_musician, name='musician'),
    path('add/',views.add_musician_view.as_view(), name='musician'),
    # path('edit/<int:id>',views.edit_musician, name='edit_musician'),
    path('edit/<int:id>',views.edit_musician_view.as_view(), name='edit_musician'),
]