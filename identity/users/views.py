from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserSignInForm, UserSignUpForm
from .decorators import logged_in_redirect
from .forms import UserUpdateForm, UserPasswordChangeForm
from .models import User, PasswordReset
from .validators import validate_email
from .utils.models import generate_random_string
from .utils.views import save_password_reset_instance


class PasswordRecoveryCodeCheckView(View):
    template = "users/check_recovery_code.html"

    @logged_in_redirect
    def get(self, request, key):
        if not PasswordReset.objects.filter(key=key).exists():
            messages.warning(request, "Invalid URL")
            return HttpResponseRedirect(reverse('users:password-recovery'))
        _next = request.GET.get('next', '/')
        msg = 'Check your inbox and enter the 6 digits code below.'
        context = {
            'next': _next,
            'message': msg,
            'pr': PasswordReset.objects.get(key=key),
        }
        return render(request, self.template, context)

    @logged_in_redirect
    def post(self, request, key):
        if not PasswordReset.objects.filter(key=key).exists():
            messages.warning(request, "Invalid URL")
            return HttpResponseRedirect(reverse('users:password-recovery'))
        pr = PasswordReset.objects.get(key=key)
        code = request.POST.get('code')
        msg = 'Check your inbox and enter the 6 digits code below.'
        if pr.is_valid and pr.code == code:
            msg = 'Enter strong passwords'
            user = pr.user
            password = generate_random_string(size=8)
            user.set_password(password)
            user.save()
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                request.session['current_password'] = password
                login(request, auth_user)
                return HttpResponseRedirect(reverse('users:change-password'))
            else:
                msg = "Something went wrong. Please try again later."
        else:
            if not pr.is_valid:
                msg = "The code is expired. Please go back and request reset code again."
            if pr.code != code:
                msg = "Invalid code. Please double check your email and enter the 6 digits code."
        _next = request.GET.get('next', '/')
        context = {
            'next': _next,
            'message': msg,
            'pr': PasswordReset.objects.get(key=key),
        }
        return render(request, self.template, context)


class PasswordRecoveryView(View):
    template = "users/password_recovery.html"

    @logged_in_redirect
    def get(self, request):
        _next = request.GET.get('next', '/')
        msg = 'Enter your email address below and we will send you an email with instructions to reset your password'
        context = {'next': _next, 'message': msg}
        return render(request, self.template, context)

    @logged_in_redirect
    def post(self, request):
        _next = request.GET.get('next', '/')
        email = request.POST.get('email')
        if not validate_email(email):
            msg = "Please enter a valid email address."
        else:
            if not User.objects.filter(email=email).exists():
                msg = "No user found"
            else:
                user = User.objects.get(email=email)
                qs = PasswordReset.objects.all().filter(user=user).order_by('-created_at')
                if qs.count() > 0:
                    last = qs.first()
                    if last.can_create_new_reset_code:
                        # send user a email here via celery task...
                        pr = save_password_reset_instance(user, request)
                        return HttpResponseRedirect(pr.get_code_check_url)
                    else:
                        msg = "You are requesting reset code too often! Please try again after 5 minutes."
                else:
                    # send user a email here via celery task...
                    pr = save_password_reset_instance(user, request)
                    return HttpResponseRedirect(pr.get_code_check_url)
        context = {'next': _next, 'message': msg}
        return render(request, self.template, context)


class ChangePassword(View):
    template = 'users/change_password.html'

    def get(self, request):
        cpass = request.session.get('current_password', None)
        resetting_password = True if cpass is not None else False
        form = UserPasswordChangeForm()
        return render(request, self.template, {'form': form, 'resetting_password': resetting_password})

    def post(self, request):
        cpass = request.session.get('current_password', None)
        resetting_password = True if cpass is not None else False
        form = UserPasswordChangeForm(request.POST)
        if form.is_valid():
            current_pass = cpass if cpass is not None else form.cleaned_data.get('current_password')
            new_pass = form.cleaned_data.get('new_password')
            if request.user.check_password(current_pass):
                request.user.set_password(new_pass)
                request.user.save()
                # destroy current password session that is being
                # followed from password recovery from code!
                request.session['current_password'] = None
                messages.success(request, "<strong>Success.</strong> Your password has been updated.")
                return HttpResponseRedirect(reverse('users:change-password'))
            else:
                form.add_error(None, "Incorrect current password.")
        return render(request, self.template, {'form': form, 'resetting_password': resetting_password})


class ProfileHome(View):
    template = 'users/home.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            # email already exists check except this account
            if User.objects.all().exclude(email=request.user.email).filter(email=email).exists():
                form.add_error(None, "Email already exists!")
            else:
                form.save()
                messages.success(request, "<strong>Success.</strong> Information has been updated")
                return HttpResponseRedirect(reverse('users:home'))
        return render(request, self.template, {'form': form})


class SignInView(View):
    template = "users/login.html"
    form = UserSignInForm()
    next = None

    @logged_in_redirect
    def get(self, request):
        """Send sign in form"""
        _next = request.GET.get('next', '/')
        context = {'form': self.form, 'next': _next}
        return render(request, self.template, context)

    @logged_in_redirect
    def post(self, request):
        """Fetch form data, validate, perform login and redirect to next page"""
        _next = request.POST.get('next', '/')
        form = UserSignInForm(request.POST)
        if form.is_valid():
            user = form.get_user(email=form.cleaned_data.get('email'))
            auth_user = authenticate(
                username=user.username,
                password=form.cleaned_data.get('password')
            )
            if auth_user is not None:
                login(request, auth_user)
                # success redirect
                response = HttpResponseRedirect(_next)
                # set user ID as cookie to track
                # user actions in webflow: www.Identity Server.com
                response.set_cookie(
                    max_age=365 * 3600 * 24,
                    key='mpuid',
                    value=request.user.id,
                    domain='localhost' if settings.DEBUG else 'Identity Server.com'
                )
                # send response
                return response
        # return context
        context = {'form': form, 'next': _next}
        return render(request, self.template, context)


class SignUpView(View):
    template = "users/register.html"
    form = UserSignUpForm()
    next = None

    @logged_in_redirect
    def get(self, request):
        """Send sign up form"""
        _next = request.GET.get('next', '/')
        context = {'form': self.form, 'next': _next}
        return render(request, self.template, context)

    @logged_in_redirect
    def post(self, request):
        """Fetch form data, validate, perform signup and redirect to next page"""
        _next = request.POST.get('next', '/')
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "<strong>Congrats!</strong> You are successfully registered!")
            success_url = reverse('users:sign-in') + f"?next={_next}"
            return HttpResponseRedirect(success_url)
        # return context
        context = {'form': form, 'next': _next}
        return render(request, self.template, context)


@login_required()
def sign_out(request):
    """Sign out user and redirect"""
    _next = request.GET.get("next", reverse('users:sign-in'))
    logout(request)
    return HttpResponseRedirect(_next)
