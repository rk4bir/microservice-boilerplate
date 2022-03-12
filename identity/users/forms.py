from django import forms
from django.contrib.auth import get_user_model
from .validators import validate_email, has_letter_character, has_numeric_character

import re


def user_exists(email):
    """Check if user exists"""
    return get_user_model().objects.filter(username=email).exists()


class UserUpdateForm(forms.ModelForm):
    """User update form"""
    photo = forms.ImageField(
        required=False,
        label="",
        widget=forms.FileInput(
            attrs={
                'id': 'photo',
                'style': "display: none",
                'accept': "image/x-png,image/gif,image/jpeg,image/jpg"
            }
        )
    )
    first_name = forms.CharField(
        required=True,
        label="First name",
        widget=forms.TextInput(
            attrs={
                'id': 'first_name',
                'placeholder': "First name",
                'onblur': "this.placeholder='First name'",
                'onfocus': "this.placeholder=''",
                'class': "form-control",
                'autocomplete': 'false'
            }
        )
    )
    last_name = forms.CharField(
        required=True,
        label="Last name",
        widget=forms.TextInput(
            attrs={
                'id': 'last_name',
                'placeholder': "Last name",
                'onblur': "this.placeholder='Last name'",
                'onfocus': "this.placeholder=''",
                'class': "form-control",
                'autocomplete': 'false'
            }
        )
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.TextInput(
            attrs={
                'id': 'email',
                'placeholder': "Email",
                'onblur': "this.placeholder='Email'",
                'onfocus': "this.placeholder=''",
                'class': "form-control",
                'autocomplete': 'false'
            }
        )
    )
    phone = forms.CharField(
        required=True,
        label="Phone",
        widget=forms.TextInput(
            attrs={
                'id': 'phone',
                'placeholder': "Phone",
                'onblur': "this.placeholder='Phone'",
                'onfocus': "this.placeholder=''",
                'class': "form-control",
                'autocomplete': 'off'
            }
        )
    )

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 3:
            raise forms.ValidationError("Too short first name")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) < 3:
            raise forms.ValidationError("Too short last name")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not validate_email(email):
            raise forms.ValidationError("Invalid email format.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        regex = re.compile(r'^[0-9]{6,}$')
        if not regex.match(phone):
            raise forms.ValidationError("Please enter a valid numeric phone number.")
        return phone

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'phone', 'photo']


class UserSignUpForm(forms.Form):
    """User sign up form"""
    first_name = forms.CharField(
        required=True,
        label="First name",
        widget=forms.TextInput(
            attrs={
                'id': 'first_name',
                'placeholder': "First name",
                'onblur': "this.placeholder='First name'",
                'onfocus': "this.placeholder=''",
                'class': "form-control",
                'autocomplete': 'false'
            }
        )
    )
    last_name = forms.CharField(
        required=True,
        label="Last name",
        widget=forms.TextInput(
            attrs={
                'id': 'last_name',
                'placeholder': "Last name",
                'onblur': "this.placeholder='Last name'",
                'onfocus': "this.placeholder=''",
                'class': "form-control",
                'autocomplete': 'false'
            }
        )
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.TextInput(
            attrs={
                'id': 'email',
                'placeholder': "Email",
                'onblur': "this.placeholder='Email'",
                'onfocus': "this.placeholder=''",
                'class': "form-control",
                'autocomplete': 'false'
            }
        )
    )
    password = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'placeholder': "Password",
                'onblur': "this.placeholder='Password'",
                'onfocus': "this.placeholder=''",
                'class': "form-control",
                'autocomplete': 'off'
            }
        )
    )

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 3:
            raise forms.ValidationError("Too short first name")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) < 3:
            raise forms.ValidationError("Too short last name")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not validate_email(email):
            raise forms.ValidationError("Invalid email format.")
        if get_user_model().objects.filter(username=email).exists()\
                or get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("User already exists!")
        return email

    def clean_password(self):
        """Validate password and return password"""
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError("Too short password")
        if not has_letter_character(password):
            raise forms.ValidationError("Password must contain at least one letter")
        if not has_numeric_character(password):
            raise forms.ValidationError("Password must contain at least one number")
        return password

    def save(self, commit=True):
        data = self.cleaned_data
        user = get_user_model()(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            username=data['email'],
            is_customer=True
        )
        user.set_password(data['password'])
        if commit:
            user.save()
        return user


class UserSignInForm(forms.Form):
    """User sign in form"""
    # email field
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.TextInput(
            attrs={
                'id': 'email',
                'placeholder': "Email",
                'onblur': "this.placeholder='Email'",
                'onfocus': "this.placeholder=''",
                'class': "form-control",
                'autocomplete': 'false'
            }
        )
    )
    # password field
    password = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'placeholder': "Password",
                'onblur': "this.placeholder='Password'",
                'onfocus': "this.placeholder=''",
                'class': "form-control",
                'autocomplete': 'false'
            }
        )
    )

    def clean_email(self):
        """
        Validate email field, check if user can login and return email
        NB: only admin and manufacturer can login here...
        """
        email = self.cleaned_data.get('email')
        if self.get_user(email) is None:
            raise forms.ValidationError("Incorrect credentials")
        if not self.can_login:
            raise forms.ValidationError("You are not authorized to sign in! Contact us for more information.")
        return email

    def clean_password(self):
        """Validate password and return password"""
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        user = self.get_user(email)
        if user is not None:
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect credentials")
        return password

    @property
    def can_login(self):
        """Check if user exists, check if user is active"""
        email = self.cleaned_data.get('email')
        user = self.get_user(email)
        if user is not None:
            return user.is_active
        return False

    @staticmethod
    def get_user(email):
        email_ck = get_user_model().objects.filter(email=email).exists()
        username_ck = get_user_model().objects.filter(username=email).exists()
        if email_ck:
            return get_user_model().objects.get(email=email)
        if username_ck:
            return get_user_model().objects.get(username=email)
        return None


class UserPasswordChangeForm(forms.Form):
    """User change password form"""
    current_password = forms.CharField(
        required=False,
        label="Current password",
        widget=forms.PasswordInput(
            attrs={
                'id': 'current_password',
                'placeholder': "Current password",
                'onblur': "this.placeholder='Current password'",
                'onfocus': "this.placeholder=''",
                'class': "form-control",
                'autocomplete': 'false',
            }
        )
    )
    new_password = forms.CharField(
        required=True,
        label="New password",
        widget=forms.PasswordInput(
            attrs={
                'id': 'new_password',
                'placeholder': "New password",
                'onblur': "this.placeholder='New password'",
                'onfocus': "this.placeholder=''",
                'class': "form-control",
                'autocomplete': 'false'
            }
        )
    )
    confirm_password = forms.CharField(
        required=True,
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                'id': 'confirm_password',
                'placeholder': "Confirm assword",
                'onblur': "this.placeholder='Confirm password'",
                'onfocus': "this.placeholder=''",
                'class': "form-control",
                'autocomplete': 'false'
            }
        )
    )

    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        if len(new_password) < 6:
            raise forms.ValidationError("Too short password")
        if not has_letter_character(new_password):
            raise forms.ValidationError("Password must contain at least one letter")
        if not has_numeric_character(new_password):
            raise forms.ValidationError("Password must contain at least one number")
        return new_password

    def clean_confirm_password(self):
        npass = self.cleaned_data.get('new_password')
        cpass = self.cleaned_data.get('confirm_password')
        if npass != cpass:
            raise forms.ValidationError("Password didn't matched.")
