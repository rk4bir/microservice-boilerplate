from django.utils.text import slugify


def app_icon_upload_dir(instance, filename):
    """
    oauth2-application model's icon save path generator
    Path structure: /media/applications/<name_id>/<filename.extension>
    """
    app_dir_title = slugify(instance.name) + f"_{instance.id}"
    return f'applications/{app_dir_title}/{filename}'
