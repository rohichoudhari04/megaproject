from django.urls import path

from . import views
#django inbuilt functionality for password reset
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('login', views.login, name='login'),
    path('approval/', views.approval, name='approval'),
               #urls path for password reset
    path("password-reset", auth_views.PasswordResetView.as_view(
        template_name="pwd/password_reset.html"), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="pwd/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(
        template_name="pwd/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="pwd/password_reset_complete.html"), name="password_reset_complete")

]
