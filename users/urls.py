from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, VerifyCodeView, UserUpdateView, get_new_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify_code/', VerifyCodeView.as_view(), name='verify_code'),
    path('get_new_password', get_new_password, name='get_new_password'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    #path('profile/genpassword/', generate_new_password, name='generate_new_password'),
]
