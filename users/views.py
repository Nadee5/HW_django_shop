import random

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse

from django.views import View
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm, NewPasswordForm
from users.models import User
from users.utils import make_verification_code


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:verify_code')
    template_name = 'users/register.html'

    def form_valid(self, form: UserRegisterForm):
        new_user = form.save()

        # verification_code = make_verification_code()
        send_mail(
            subject='Подтверждение регистрации',
            message=f'Код подтверждения почты для доступа на сайт: {new_user.verify_code}.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
        )
        return super().form_valid(form)


class VerifyCodeView(View):
    model = User
    template_name = 'users/verify_code.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *agrs, **kwargs):
        verify_code = request.POST.get('verify_code')
        user = User.objects.filter(verify_code=verify_code).first()
        if user:
            user.is_verified = True
            user.save()
            return redirect('users:login')

        return redirect('users:verify_code')


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserProfileForm

    def get_object(self, queryset=None): #избавляет от необходимости ввода pk, редактирует текущего юзера
        return self.request.user


# def generate_new_password(request):
#     new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
#     send_mail(
#         subject='Вы сменили пароль',
#         message=f'Ваш новый пароль: {new_password}',  # {new_user.verify_code}
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[request.user.email],
#     )
#     request.user.set_password(new_password)
#     request.user.save()
#     return redirect(reverse('shop:home'))


def get_new_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        # new_password = BaseAbstractUser().manager.make_random_password()
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        send_mail(
            subject='Пароль изменён',
            message=f'Ваш новый пароль: {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        user.set_password(new_password)
        user.save()
        return redirect(reverse('users:login'))
    else:
        form = NewPasswordForm
        context = {
            'form': form,
        }
        return render(request, 'users/new_password.html', context)


















