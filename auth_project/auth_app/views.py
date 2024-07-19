from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.views import View
import os

from .models import CustomUser
from .forms import RegisterForm, CustomAuthenticationForm

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            # login(request, user)
            return redirect('login')
        return render(request, 'registration/register.html', {'form': form})




class LoginView(View):
    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, 'registration/login.html', {'form': form})




class ForgotPasswordView(View):
    def get(self, request):
        return render(request, 'registration/forgot_password.html')

    def post(self, request):

        email = request.POST.get('email')
        user = get_object_or_404(CustomUser, email=email)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        reset_url = f"http://{request.get_host()}/auth/reset-password/{uid}/{token}/"

        # Email configuration
        smtp_server = os.getenv('EMAIL_HOST')
        smtp_port = 587
        sender_email = os.getenv('EMAIL_HOST_USER')
        receiver_email = user.email
        password = os.getenv('EMAIL_HOST_PASSWORD')

        subject = 'Password Reset Link'
        body = f'Use this link to reset your password: {reset_url}'
        
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = user.email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
        finally:
            server.quit()
            
        return redirect('login')




class ChangePasswordView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_object_or_404(CustomUser, pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            form = SetPasswordForm(user)
            return render(request, 'registration/change_password.html', {'form': form})
        else:
            return redirect('login')

    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_object_or_404(CustomUser, pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('login')
            else:
                return render(request, 'registration/change_password.html', {'form': form})
        else:
            return redirect('login')

