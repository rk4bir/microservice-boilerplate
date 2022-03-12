from ..models import PasswordReset


def save_password_reset_instance(user, request):
    pr = PasswordReset.objects.create(user=user)
    context = {
        "reset_uri": request.build_absolute_uri(pr.get_code_check_url),
        "reset_code": pr.code
    }
    return pr


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
