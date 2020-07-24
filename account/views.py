from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.urls import reverse_lazy


class Login(auth_views.LoginView):
    template_name = 'account/login.html'
    success_url_allowed_hosts = settings.ALLOWED_HOSTS
    redirect_authenticated_user = True


class Logout(LoginRequiredMixin, auth_views.LogoutView):
    redirect_field_name = None
    template_name = 'account/logout.html'

    
class UserPassReset(auth_views.PasswordResetView):
    template_name = 'account/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'account/reset_done.html'


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'
