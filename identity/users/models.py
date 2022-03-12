from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.shortcuts import reverse


from .utils.models import generate_unique_key, generate_random_number


class User(AbstractUser):
    first_name = models.CharField(max_length=32, blank=False, null=False)
    last_name = models.CharField(max_length=32, blank=False, null=False)
    username = models.CharField(max_length=32, blank=False, null=False, unique=True)
    email = models.CharField(max_length=255, blank=False, null=False, unique=True)
    phone = models.CharField(max_length=32, blank=True, null=True, unique=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True, auto_now_add=False)

    @property
    def user_type(self):
        return "admin" if self.is_superuser else "user"

    def __str__(self):
        return self.username


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=128, blank=True, null=True, unique=True)
    code = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"PasswordReset - {self.user}"

    @property
    def get_code_check_url(self):
        return reverse('users:reset-code-check', kwargs={'key': self.key})

    @property
    def is_valid(self):
        """Reset link expires after 30 minutes"""
        diff = timezone.now() - self.created_at
        minutes = diff.total_seconds() // 60
        if minutes <= 30:
            return True
        return False

    @property
    def can_create_new_reset_code(self):
        """Can't request password reset before 5 minutes"""
        diff = timezone.now() - self.created_at
        minutes = diff.total_seconds() // 60
        if minutes > 5:
            return True
        return False


def password_reset_pre_save_action(sender, instance, *args, **kwargs):
    if not instance.key:
        instance.key = generate_unique_key(instance)
    if not instance.code:
        instance.code = generate_random_number(size=6)


pre_save.connect(password_reset_pre_save_action, PasswordReset, weak=False)
