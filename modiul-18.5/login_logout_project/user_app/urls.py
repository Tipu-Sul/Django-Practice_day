from django.urls import path
from. import views

urlpatterns = [
    path('signup/',views.signUp,name='signup' ),
    path('login/',views.user_login,name='login' ),
    path('profile/',views.profile,name='profile' ),
    path('profile/edit_user/',views.editProfile,name='edit_user' ),
    path('profile/edit_pass/',views.passChange,name='passChange' ),
    path('profile/edit_pass2/',views.passChange2,name='passChange2' ),
    path('logout/',views.user_logout,name='logout' ),
   
]
