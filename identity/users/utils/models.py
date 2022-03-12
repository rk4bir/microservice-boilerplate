import random
import string


def generate_random_string(size=32):
    choice_string = string.digits + string.ascii_letters
    return ''.join([random.choice(choice_string) for _ in range(size)])


def generate_unique_key(instance):
    klass = instance.__class__
    key = generate_random_string(size=100)
    if klass.objects.filter(key=key).exists():
        return generate_unique_key(instance)
    return key


def generate_random_number(size=16):
    return ''.join([random.choice(string.digits) for _ in range(size)])


def generate_unique_tracking_id(instance, size=16):
    klass = instance.__class__
    tid = generate_random_number(size=size)
    if klass.objects.filter(tracking_id=tid).exists():
        return generate_unique_tracking_id(instance, size=size)
    return tid


def user_photo_upload_dir(instance, filename):
    """
    User model's photo save path generator
    Path structure: /media/users/<username>/<filename.extension>
    """
    print(f'users/{instance.username}/{filename}')
    return f'users/{instance.username}/{filename}'
