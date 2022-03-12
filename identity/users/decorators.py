from django.shortcuts import HttpResponseRedirect, reverse


def logged_in_redirect(view_func):
    """
    Redirect to previous page if the is already logged in,
    this decorator is created to use inside cases methods for
    (login, registration) views.
    """
    def wrapper(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("users:home"))
        return view_func(self, request, *args, **kwargs)
    return wrapper
