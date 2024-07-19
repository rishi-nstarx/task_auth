# # auth_app/urls.py
# from django.urls import path
# from .views import login_view, logout_view, forgot_password_view, reset_password_view, change_password_view

# urlpatterns = [
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
#     path('forgot_password/', forgot_password_view, name='forgot_password'),
#     path('reset_password/', reset_password_view, name='reset_password'),
#     path('change_password/', change_password_view, name='change_password'),
# ]


# users/urls.py
from django.urls import path
from .views import RegisterView, LoginView, ForgotPasswordView, ChangePasswordView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/<uidb64>/<token>/', ChangePasswordView.as_view(), name='change-password'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
