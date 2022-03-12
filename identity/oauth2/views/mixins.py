from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied


class IsSuperUserMixin(AccessMixin):
    """Deny request with a permission error if the user is not superuser"""

    def handle_none_superuser(self):
        if self.raise_exception:
            raise PermissionDenied("You are not authorized to perform the action")
        return HttpResponseRedirect(reverse_lazy('users:home'))

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        result = user.is_superuser and user.is_staff
        if not result:
            return self.handle_none_superuser()
        return super().dispatch(request, *args, **kwargs)
