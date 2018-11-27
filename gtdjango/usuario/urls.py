from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from django.contrib.auth import urls

from .views import UsuarioCreateView

urlpatterns = [

    path('login/', LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('registrar/', UsuarioCreateView.as_view(), name="registrar"),

    path('password_reset/', PasswordResetView.as_view(template_name='usuario/password_reset_form.html',
                                                      email_template_name='usuario/password_reset_email.html'),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='usuario/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='usuario/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='usuario/password_reset_complete.html'), name='password_reset_complete'),
]
